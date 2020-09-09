from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from core import models
import json
from core.urls import *
# Create your views here.

@login_required(login_url= '/login/')
def index_view(request):
    to_chat_users = models.Follow.objects.filter(follower=request.user)
    return render(request, 'chat/index.html', {
        'to_chat_users': to_chat_users
    })


def room_view(request, user_name):
    return render(request, 'chat/room.html', {
        'user_name_json': mark_safe(json.dumps(user_name))
    })

