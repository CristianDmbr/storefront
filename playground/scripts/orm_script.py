from playground.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models.functions import Lower, Length
import random
from django.db.models.functions import Upper, Length, Concat, Coalesce
from django.db.models import Count, Avg, Min, Max, CharField, Value, Case, When, Sum, F, Q, OuterRef, Subquery, Exists
from django.contrib.contenttypes.models import ContentType


def run():
    allContentTypes = ContentType.objects.all()

    content_types = ContentType.objects.filter(app_label = 'playground')
    

    content = ContentType.objects.get(
        app_label = 'playground', model = 'restaurant'
    )

    restaurantModel = content.model_class()
    print(restaurantModel.objects.all())

    specificRestaurant = content.get_object_for_this_type(name = 'Golden Dragon')
    print(specificRestaurant)
    print(specificRestaurant.longitute)