from django.db import models
from django.contrib.auth.models import User

class ChatSession(models.Model):
    """
    Represents a chat session 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='')
    date = models.DateField(auto_now_add=True)

class Message(models.Model):
    """
    Represents a single message in a chat session.
    """
    chat_session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)  # e.g., 'user' or 'bot'
    content = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
