from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_detail, name='product_detail'),
    path('delete/<int:pk>', views.delete_chat, name='chat_delete'),
]

