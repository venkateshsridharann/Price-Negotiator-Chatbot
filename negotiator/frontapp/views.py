from django.shortcuts import render
from .models import Product

def display_products(request):
    products = Product.objects.all()
    return render(request, 'frontapp/product_display.html', {'products': products})