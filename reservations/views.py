from datetime import datetime
from django.shortcuts import render, redirect
from .models import Reservations
from django.contrib import messages
from clients import models
import re


def reservation(request):
    if request.method == 'POST':
        id = request.POST.get('room_id')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        start_date = request.POST['start-date']
        end_date = request.POST['end-date']
        breakfast = True if request.POST.get('breakfast') == 'on' else False
        all_inclusive = True if request.POST.get(
            'all-inclusive') == 'on' else False
        price = request.POST.get('price')
        price_regex = r'^\d+\.\d{1,2}'
        match = re.search(price_regex, price)
        cost = float(match.group(0))

        if datetime.strptime(end_date, '%Y-%m-%d').date() <= datetime.strptime(start_date, '%Y-%m-%d').date():
            return render(request, 'reservation.html', {'InvalidDates': 'End date must be after the start date.', 'id': id, 'price': cost})

        if breakfast == True:
            cost += 5
        if all_inclusive == True:
            cost += 10
        reservation = Reservations(reserved_room=id,
                                   username=username,
                                   start_date=start_date,
                                   end_date=end_date,
                                   including_breakfast=breakfast,
                                   all_inclusive=all_inclusive,
                                   cost=cost)
        reservation.save()
        try:
            client_exist = models.Clients.objects.get(first_name=first_name,
                                                      last_name=last_name,
                                                      phone=phone,
                                                      email=email)
            messages.success(
                request, 'Congratulations! Your reservation has been confirmed.')

            return redirect('home')
        except:
            clients = models.Clients(first_name=first_name,
                                     last_name=last_name,
                                     phone=phone,
                                     email=email)
            clients.save()
            messages.success(
                request, 'Congratulations! Your reservation has been confirmed.')

            return redirect('home')
    else:
        return render(request, 'reservation.html', {'InvalidDates': ''})
