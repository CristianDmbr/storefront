from playground.models import Restaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection

def run():
    restaurant = Restaurant.objects.first()
    print(restaurant.pk)
    print(restaurant.rating.all())
    restaurant.delete()
    

    print(connection.queries) 