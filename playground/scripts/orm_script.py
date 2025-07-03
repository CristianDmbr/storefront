from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower

def run():
    staff, created = Staff.objects.get_or_create(name = "John Wich")
    restaurant = Restaurant.objects.first()
    restaurant2 = Restaurant.objects.last()
    
    StaffRestaurant.objects.create(
        staff = staff, restaurant = restaurant, salary = 28000
    )

    StaffRestaurant.objects.create(
        staff = staff, restaurant = restaurant2, salary = 30000
    )