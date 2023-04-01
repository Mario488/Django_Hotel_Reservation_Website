from django.shortcuts import render, redirect
from . models import Room
from django.contrib import messages


def rooms(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            room_id = request.POST.get('room_id')
            room_price = request.POST.get('price')
            return render(request, 'reservation.html', {'id': room_id, 'price': room_price, 'username': request.user.username, 'email': request.user.email})
        else:
            messages.warning(
                request, 'Please login before making a reservation!')
            return redirect('login')
    else:
        rooms = Room.objects.all()
        context = {'rooms': rooms}
        return render(request, 'rooms.html', context)
