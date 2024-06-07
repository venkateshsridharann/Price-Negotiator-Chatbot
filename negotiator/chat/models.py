from django.db import models
from frontapp.models import Product

class ChatSession(models.Model):
    """
    Represents a chat session associated with a product.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='chat_sessions')
    content = models.TextField(default='')

class Message(models.Model):
    """
    Represents a single message in a chat session.
    """
    chat_session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)  # e.g., 'user' or 'bot'
    content = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
