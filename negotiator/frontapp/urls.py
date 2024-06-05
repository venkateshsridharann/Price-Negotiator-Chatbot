# your_app/urls.py
from django.urls import path
from .views import display_products, custom_logout

urlpatterns = [
    path('', display_products, name='display_products'),
    path('logout/', custom_logout, name='custom_logout'),
]