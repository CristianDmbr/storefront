from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper
from django.db.models import Count, Avg, Min, Max


def run():
    # Fetch all restaurants and want to get the number of characters in the name of the restaurant. e.g. 'xyz' == 3
    