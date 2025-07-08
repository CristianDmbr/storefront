from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.functions import Lower



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

    class Meta:
        ordering = [Lower('name')]


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)

class Staff(models.Model):
    name = models.CharField(max_length = 128)
    restaurants = models.ManyToManyField(Restaurant, through = 'StaffRestaurant')


    def __str__(self):
        return self.name

class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    salary = models.FloatField(null = True)


# Create a ratings model for storing different user ratings for restaurants
# Its going to store a reference to the user who made the rating and the restaurant which the rating applies to
# Table will contain two foreign keys to those two different tables

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = 'ratings')
    rating = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Rating : {self.rating}"

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.SET_NULL, null = True, related_name = 'sales')
    income = models.DecimalField(max_digits=8,decimal_places=2)
    expenditure = models.DecimalField(max_digits = 8, decimal_places= 2)
    dateTime = models.DateTimeField()
