from django.shortcuts import render
from .forms import RatingForm
from playground.models import Restaurant, Sale, Rating
from django.db.models import Sum, Prefetch
from django.utils import timezone

def index(request):
    # Get all 5 star ratings and fetch all sales for restaurants
    monthAgo = timezone.now() - timezone.timedelta(days = 30)
    monthly_sales = Prefetch(
        'sales',
        queryset = Sale.objects.filter(dataOpened__gte = monthAgo)
    )
    
    restaurants = Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(rating__rating = 5)
    print(restaurants)

    
    return render(request, 'index.html')