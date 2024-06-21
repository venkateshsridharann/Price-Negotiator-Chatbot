from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chats, name='all_chats'),
    path('delete/<int:pk>', views.delete_chat, name='chat_delete'),
    path('edit/<int:pk>', views.chat_edit, name='chat_edit'),
    path('add_chat/', views.add_chat, name='add_chat'),
    path('<int:pk>', views.load_chat, name='load_chat'),
    path('send_message/', views.send_message, name='send_message'),
   
]

