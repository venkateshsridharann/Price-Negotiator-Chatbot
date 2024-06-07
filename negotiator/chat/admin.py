from django.contrib import admin
from .models import ChatSession, Message

admin.site.register(ChatSession)
admin.site.register(Message)