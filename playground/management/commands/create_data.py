import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from playground.models import Restaurant, Rating, Sale


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create an admin user
        user = User.objects.filter(username='admin')
        if not user.exists():
            user = User.objects.create_superuser(username='admin', password='test')
        else:
            user = user.first()

        Restaurant.objects.all().delete()

        restaurants = [
            {'name': 'Pizzeria 1', 'dataOpened': timezone.now() - timezone.timedelta(days=20), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitute': 55.869829854, 'longitute': -4.28583219},
            {'name': 'Pizzeria 2', 'dataOpened': timezone.now() - timezone.timedelta(days=27), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitute': 55.862, 'longitute': -4.247},
            {'name': 'Golden Dragon', 'dataOpened': timezone.now() - timezone.timedelta(days=15), 'restaurant_type': Restaurant.TypeChoices.CHINESE, 'latitute': 55.953251, 'longitute': -3.188267},
            {'name': 'Bombay Bustle', 'dataOpened': timezone.now() - timezone.timedelta(days=44), 'restaurant_type': Restaurant.TypeChoices.INDIAN, 'latitute': 51.509865, 'longitute': -0.118092},
            {'name': 'Chinese 2', 'dataOpened': timezone.now() - timezone.timedelta(days=31), 'restaurant_type': Restaurant.TypeChoices.CHINESE, 'latitute': 53.400002, 'longitute': -2.983333},
            {'name': 'Chinese 3', 'dataOpened': timezone.now() - timezone.timedelta(days=71), 'restaurant_type': Restaurant.TypeChoices.CHINESE, 'latitute': 55.070859, 'longitute': -3.60512},
            {'name': 'Indian 2', 'dataOpened': timezone.now() - timezone.timedelta(days=46), 'restaurant_type': Restaurant.TypeChoices.INDIAN, 'latitute': 53.350140, 'longitute': -6.266155},
            {'name': 'Pizzeria 3', 'dataOpened': timezone.now() - timezone.timedelta(days=4), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitute': 54.966667, 'longitute': -1.600000},
            {'name': 'Pizzeria 4', 'dataOpened': timezone.now() - timezone.timedelta(days=61), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitute': 48.856614, 'longitute': 2.3522219},
            {'name': 'Italian 1', 'dataOpened': timezone.now() - timezone.timedelta(days=37), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitute': 41.902782, 'longitute': 12.496366},
        ]

        for r in restaurants:
            Restaurant.objects.create(**r)

        restaurants = Restaurant.objects.all()

        # create ratings
        for _ in range(30):
            Rating.objects.create(
                restaurant=random.choice(restaurants),
                user=user,
                rating=random.randint(1, 5)
            )

        # create sales
        for _ in range(100):
            Sale.objects.create(
                restaurant=random.choice(restaurants),
                income=round(random.uniform(5, 100), 2),
                dateTime=timezone.now() - timezone.timedelta(days=random.randint(1, 50))
            )