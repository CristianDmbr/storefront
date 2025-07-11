from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper, Length, Concat, Coalesce
from django.db.models import Count, Avg, Min, Max, CharField, Value, Case, When, Sum, F, Q, OuterRef, Subquery, Exists


def run():
    # Filter restaurants that have sales with income of more than 85.
    restaurants = Restaurant.objects.filter(
        Exists(Sale.objects.filter(restaurant = OuterRef('pk'), income__gt = 90))
    )

    print(restaurants)
    