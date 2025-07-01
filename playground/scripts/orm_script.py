from playground.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower

def run():

    restaurants = Restaurant.objects.order_by(Lower('name'))
    print(restaurants)
     
    print(connection.queries)