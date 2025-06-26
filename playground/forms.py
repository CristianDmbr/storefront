from django import forms
from .models import Rating
from django.core.validators import MaxValueValidator, MinValueValidator

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('restaurant', 'user', 'rating')

class RatingForm(forms.Form):
    rating = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])