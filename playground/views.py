from django.shortcuts import render, redirect
from playground.models import Restaurant, Sale, Rating, StaffRestaurant
from django.db.models import Sum, Prefetch
from django.utils import timezone
from .forms import ProductOrderForm
from django.db import transaction
from functools import partial

def email_user(email):
    print(f'Dear {email}, Thank you for your order.')

def greet(name, surname):
    print(f'Hello {name} {surname} welcome!')

def index(request):
    jobs = StaffRestaurant.objects.prefetch_related('restaurant','staff')

    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)

    return render(request, 'index.html')

def order_product(request):
    if request.method == 'POST':
        form = ProductOrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()
                order.product.numberInStock -= order.numberOfItems
                order.product.save()
            
            transaction.on_commit(partial(greet,'Cristian','Dumbravanu'))

            return redirect('order-product')
        else:
            context = {'form' : form}
            return render(request, 'order.html', context) 

     
    form = ProductOrderForm()
    context = {'form' : form}
    return render(request, 'order.html', context) 