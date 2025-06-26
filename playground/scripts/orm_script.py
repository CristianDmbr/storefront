from playground.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection

def run():
    restaurant = Restaurant.objects.first()
    print(restaurant.sales.all())