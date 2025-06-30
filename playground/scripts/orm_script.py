from playground.models import Restaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection

def run():
    restaurant = Restaurant.objects.first()

    restaurant.name = 'New Restaurant Name'
    restaurant.save(update_fields = ['name'])
