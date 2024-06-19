from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chats, name='all_chats'),
    path('delete/<int:pk>', views.delete_chat, name='chat_delete'),
    path('add_chat/', views.add_chat, name='add_chat'),
]

