from django import forms
from .models import Rating, Order, Product
from django.core.validators import MaxValueValidator, MinValueValidator

class ProductStockException(Exception):
    pass

class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product','numberOfItems')

    def save(self, commit = True):
            # Check if the product has enough items in stock
            order = super().save(commit = False)
            if order.product.numberInStock < order.numberOfItems:
                raise ProductStockException(
                    f"Not enough items in stock for product : {order.product}"
                )
            if commit :
                order.save()
            return order