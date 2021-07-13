import random
from django.shortcuts import render
from datetime import datetime
from .models import Contact, Purchase, Products
from django.contrib import messages


def new(request):
    new = Products.objects.filter(date__gte='2021-07-13')
    return render(request, "new.html",
                  {'new': new})


def laptops(request):
    laptops = Products.objects.filter(category='LAPTOP')
    return render(request, "laptops.html",
                  {'laptops': laptops})


def mobiles(request):
    mobiles = Products.objects.filter(category='MOBILE')
    return render(request, "mobiles.html",
                  {'mobiles': mobiles})


def leds(request):
    leds = Products.objects.filter(category='LED')
    return render(request, "leds.html",
                  {'leds': leds})


def index(request):
    return render(request, "index.html")


def trending(request):
    trend = Products.objects.all()
    return render(request, "trending.html",
                  {'trend': trend})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

    return render(request, "contact.html")


def products(request):
    products = list(Products.objects.all())
    products = random.sample(products, 9)
    return render(request, "products.html",
                  {'products': products})


def purchase(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        desc = request.POST.get('desc')
        purchase = Purchase(name=name, email=email, phone=phone, amount=amount, desc=desc, date=datetime.today())
        purchase.save()
        messages.success(request, 'Purchase Made Successfully !!!')
    return render(request, "purchase.html")