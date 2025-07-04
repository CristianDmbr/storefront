from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower
import random
from django.db.models.functions import Upper


def run():
    restaurants = Restaurant.objects.values_list('name','dataOpened')
    print(restaurants)