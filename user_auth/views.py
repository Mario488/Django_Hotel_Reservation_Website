from django.shortcuts import render, redirect
from users import models
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_method
from django.contrib.auth import login as login_method
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from reservations import models as res_model
from rooms import models
from django.urls import reverse_lazy


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.info(self.request, 'Password Changed Successfully!')
        return super().form_valid(form)


def passwordChange(request):
    return MyPasswordChangeView.as_view()(request)


def profile(request):
    if request.method == 'POST':
        username = request.user.username
        reserved_room = request.POST['room_id']
        res_del = res_model.Reservations.objects.filter(
            reserved_room=reserved_room,
            username=username)
        res_del.delete()
        return redirect('profile')
    curr_user = request.user
    username = curr_user.username
    email = curr_user.email

    reservations = res_model.Reservations.objects.filter(username=username)
    reservation_ids = [
        reservation.reserved_room for reservation in reservations]

    cost = [i.cost for i in reservations]

    rooms = models.Room.objects.filter(id__in=reservation_ids)

    room_reserv = zip(rooms, reservations)

    context = {'username': username,
               'email': email,
               'reserv': room_reserv,
               'cost': sum(cost)}

    return render(request, 'profile.html', context)


def logout(request):
    print('Logout view called')
    logout_method(request)
    messages.success(request, 'You\'ve been logged out')
    return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_method(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('home')
        else:
            return render(request, 'login.html', {'message': 'Invalid username or password!'})
    return render(request, 'login.html', {'message': ''})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'sign_up.html', {'form': form})
