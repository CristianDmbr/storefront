from django.contrib import admin
from playground.models import Restaurant, Sale, Rating, Product, Order, Comment
from django.contrib.contenttypes.admin import GenericTabularInline

class CommentInline(GenericTabularInline):
    model = Comment
    max_num = 1 

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    inlines = [CommentInline] 

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','rating']

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'text','object_id','content_type','content_object'
    ]

# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Sale)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment, CommentAdmin)