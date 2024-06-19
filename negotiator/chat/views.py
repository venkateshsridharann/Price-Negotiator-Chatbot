from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import ChatSession, Message
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from datetime import datetime

import json



@login_required
def all_chats(request):
    # Filter chat sessions by the logged-in user
    chat_sessions = ChatSession.objects.filter(user=request.user)
    return render(request, 'chat_interface.html', { 'chat_sessions': chat_sessions})


@login_required
def delete_chat(request, pk):
    item = get_object_or_404(ChatSession, pk=pk)
    messages =  messages_to_delete = Message.objects.filter(chat_session=pk)
    messages_to_delete.delete()
    item.delete()
    return redirect('/chat')

@login_required
def add_chat(request):
    current_datetime = str(datetime.now())[:16]
    new_chat_session = ChatSession.objects.create(user=request.user, content="Chat dated "+ current_datetime)
    # Redirect to the chat interface
    return redirect(reverse('all_chats'))

