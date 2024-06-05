from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required
def display_products(request):
    products = Product.objects.all()
    return render(request, 'frontapp/product_display.html', {'products': products})


def custom_logout(request):
    logout(request)
    return redirect('/') 