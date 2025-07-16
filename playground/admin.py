from django.contrib import admin
from playground.models import Restaurant, Sale, Rating, Product, Order, Comment

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','rating']

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'text','objectId','content_type','content_object'
    ]

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Rating)
admin.site.register(Product)
admin.site.register(Order)
 