from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant, Comment, Task, TaskStatus, InProgressTask
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper, Length, Concat, Coalesce
from django.db.models import Count, Avg, Min, Max, CharField, Value, Case, When, Sum, F, Q, OuterRef, Subquery, Exists
from django.contrib.contenttypes.models import ContentType


def run():
    in_progress = InProgressTask.objects.create(name = "Watch starwards")
    print(in_progress)