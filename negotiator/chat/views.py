from django.shortcuts import render, get_object_or_404
from frontapp.models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'chat_interface.html', {'product': product})