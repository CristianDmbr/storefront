from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper, Length, Concat
from django.db.models import Count, Avg, Min, Max, CharField, Value, Case, When, Sum, F


def run():
    rating = Rating.objects.filter(rating = 3).first()