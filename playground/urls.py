from django.urls import path
from . import views

#URL configuration
urlpatterns = [
    path('', views.index, name = 'index'),
    path('order/', views.order_product, name = 'order-product'),
] 