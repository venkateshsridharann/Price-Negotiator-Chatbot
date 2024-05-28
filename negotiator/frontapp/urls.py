# your_app/urls.py
from django.urls import path
from .views import display_products

urlpatterns = [
    path('', display_products, name='display_products'),
]