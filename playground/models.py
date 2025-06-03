from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    country = models.CharField(max_length=100)

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN','Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        OTHER = 'OT', 'Other'



    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    dataOpened = models.DateField()
    latitute = models.FloatField()
    longitute = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices = TypeChoices.choices )

    def __str__(self):
        return self.name

# Create a ratings model for storing different user ratings for restaurants
# Its going to store a reference to the user who made the rating and the restaurant which the rating applies to
# Table will contain two foreign keys to those two different tables

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    rating = models.PositiveSmallIntegerField()

def __str__(self):
    return f"Rating : {self.rating}"