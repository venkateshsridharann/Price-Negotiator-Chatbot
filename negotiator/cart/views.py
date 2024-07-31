from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Use get_or_create to find the cart item or create it if it doesn't exist
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    # Increment the quantity if the cart item already exists
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1  # Set initial quantity for new cart item
    # Calculate the cartTotal
    cart_item.cartTotal = product.listed_price * cart_item.quantity
    # Save the cart item
    cart_item.save()
    return redirect('/')  # Update this line

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    grandtotal = sum(item.cartTotal for item in cart_items)
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'grandtotal': grandtotal})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    action = request.POST.get('action')

    if action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.cartTotal -= cart_item.product.listed_price
            cart_item.quantity -= 1
            cart_item.save()
    elif action == 'increase':
        cart_item.cartTotal += cart_item.product.listed_price
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'remove':
        cart_item.delete()
    
    entire_cart = CartItem.objects.filter(user=request.user)
    grandtotal = sum(item.cartTotal for item in entire_cart)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print(cart_item.cartTotal)
        return JsonResponse({
            'message': 'Cart updated successfully!',
            'new_quantity': cart_item.quantity,
            'new_cart_total': cart_item.cartTotal,
            'grandtotal': grandtotal
        })
        
    else:
        return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    grandtotal = sum(item.cartTotal for item in cart_items)
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'grandtotal': grandtotal})

