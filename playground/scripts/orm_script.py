from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant, Comment
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper, Length, Concat, Coalesce
from django.db.models import Count, Avg, Min, Max, CharField, Value, Case, When, Sum, F, Q, OuterRef, Subquery, Exists
from django.contrib.contenttypes.models import ContentType


def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating = Rating.objects.create(
        restaurant = restaurant,
        user = user,
        rating = 12412
    )