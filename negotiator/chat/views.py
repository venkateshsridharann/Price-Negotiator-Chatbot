from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import ChatSession, Message
from cart.models import CartItem
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from datetime import datetime
import json
from . import openai_chat
from django.views.decorators.csrf import csrf_exempt

@login_required
def all_chats(request):
    current_url = request.build_absolute_uri()
    url_segments = current_url.split('/')
    indicator = True if url_segments[-1] == '' else False
    # Filter chat sessions by the logged-in user
    chat_sessions = ChatSession.objects.filter(user=request.user)
    return render(request, 'chat_interface.html', { 'chat_sessions': chat_sessions, 'indicator':indicator})


@login_required
def delete_chat(request, pk):
    chat = get_object_or_404(ChatSession, pk=pk)
    messages =  messages_to_delete = Message.objects.filter(chat_session=pk)
    messages_to_delete.delete()
    chat.delete()
    return redirect('/chat')

@login_required
def add_chat(request):
    current_datetime = str(datetime.now())[:16]
    new_chat_session = ChatSession.objects.create(user=request.user, content="Chat dated "+ current_datetime)
    # Redirect to the chat interface
    new_id = str(new_chat_session.id)
    return redirect('/chat/'+new_id)

@login_required
def chat_edit(request,pk):
    messages = Message.objects.filter(chat_session=pk)
    chat_sessions = ChatSession.objects.filter(user=request.user)
    # chat to edit
    chat_session = get_object_or_404(ChatSession, id=pk)
    chat_session.save()
    if request.method == 'POST':
        updated_content = request.POST.get('updated_content', '')
        chat_session.content = updated_content
        chat_session.save()

    return redirect('/chat/'+str(pk))
    # return render(request, 'chat_interface.html', {'chat_sessions': chat_sessions, "messages":messages})



@login_required
def load_chat(request,pk):
    messages = Message.objects.filter(chat_session=pk)
    chat_sessions = ChatSession.objects.filter(user=request.user)
    return render(request, 'chat_interface.html', {'chat_sessions': chat_sessions, "messages":messages})

def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('user_input')
        sender = request.POST.get('sender')
        chat_id = request.POST.get('chat_id')
        chat_id = int(chat_id)

        cart_items = CartItem.objects.filter(user=request.user)
        grandtotal = sum(item.cartTotal for item in cart_items)
        print(grandtotal)
        chat_session = ChatSession.objects.filter(id=chat_id)[0]
        all_messages = Message.objects.filter(chat_session=chat_session)
        Message.objects.create(content=content,sender=sender,chat_session=chat_session)
        if sender=='user':
            openai_response = openai_chat.chat_with_gpt(content,all_messages,grandtotal)
            print(openai_response)
        Message.objects.create(content=openai_response,sender='bot',chat_session=chat_session)
        return JsonResponse({'status': 'success', 'message': openai_response})  # Return JSON response
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)