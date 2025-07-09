from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper, Length, Concat
from django.db.models import Count, Avg, Min, Max, CharField, Value, Case, When, Sum, F, Q


def run():
    itOrMex = Q(name__icontaints = "italian") | Q(name_icontains = "mexican")
    notRecentlyOpened = ~Q(dataOpened__gt = timezone.now() - timezone.timedelta(days = 40))

    restaurants = Restaurant.objects.filter(itOrMex | notRecentlyOpened)