from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ChatSession


@login_required
def product_detail(request):
    # Filter chat sessions by the logged-in user
    chat_sessions = ChatSession.objects.filter(user=request.user)
    return render(request, 'chat_interface.html')
    # return render(request, 'chat_interface.html', { 'chat_sessions': chat_sessions})
