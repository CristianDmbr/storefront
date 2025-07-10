from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper, Length, Concat, Coalesce
from django.db.models import Count, Avg, Min, Max, CharField, Value, Case, When, Sum, F, Q


def run():
    # Check average rating > 3.5 and restaurants have more than 1 rating

    restaurants = Restaurant.objects.annotate(averageRating = Avg('ratings__rating'), nRatings = Count('ratings__pk'))

    restaurants = restaurants.annotate(
        highlyRated = Case(
            When(averageRating__gt = 3.5, nRatings__gt = 1, then = True),
            default = False
        )
    )

    restaurants = restaurants.annotate(
        ratingBucket = Case(
            When(avg__gt = 3.5, then = Value('Highly Rated')),
            When(avg_range = (2.5, 3.5), then = Value('Average Rating')),
            When(avg_lt = 2.5, then = Value('Bad Rating')),
            default = False
        )
    )

    # Assign continets to each restaurant

    print(restaurants.filter(highlyRated = False))
    print(restaurants.filter(ratingBucket = 'Highly Rated'))