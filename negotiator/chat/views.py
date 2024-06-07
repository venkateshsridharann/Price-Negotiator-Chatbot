from django.shortcuts import render, get_object_or_404
from frontapp.models import Product
from .models import ChatSession

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    chat_sessions = ChatSession.objects.filter(product=product)
    return render(request, 'chat_interface.html', {'product': product, 'chat_sessions': chat_sessions})