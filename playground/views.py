from django.shortcuts import render
from .forms import RatingForm
from playground.models import Restaurant, Sale, Rating, StaffRestaurant
from django.db.models import Sum, Prefetch
from django.utils import timezone

def index(request):
    jobs = StaffRestaurant.objects.prefetch_related('restaurant','staff')

    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)

    return render(request, 'index.html')