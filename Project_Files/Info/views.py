from django.shortcuts import render


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    if request.method == 'POST':
        return render(request, 'contact_us.html', {'message': 'Message Sent Successfully!'})
    return render(request, 'contact_us.html', {'message': ''})
