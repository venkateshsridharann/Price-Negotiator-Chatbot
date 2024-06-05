from django.urls import path
from .views import custom_login

urlpatterns = [
    path('login/', custom_login, name='custom_login'),
]