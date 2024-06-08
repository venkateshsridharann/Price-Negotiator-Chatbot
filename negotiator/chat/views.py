from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from frontapp.models import Product
from .models import ChatSession


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    chat_sessions = ChatSession.objects.filter(product=product)
    return render(request, 'chat_interface.html', {'product': product, 'chat_sessions': chat_sessions})



def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    action = request.POST.get('action')

    if action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
    elif action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'remove':
        cart_item.delete()

    return redirect('cart_detail')