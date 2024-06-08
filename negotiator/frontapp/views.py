from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Product
from cart.models import CartItem
from django.contrib import messages

@login_required
def display_products(request):
    products = Product.objects.all()
    return render(request, 'frontapp/product_display.html', {'products': products})


def custom_logout(request):
    logout(request)
    return redirect('/') 

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.success(request, f"{product.title} has been added to your cart.")

    # Render the same product display page
    return render(request, 'product_display.html', {'product': product})
    # return redirect('/')  

