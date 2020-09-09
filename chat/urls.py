from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('<str:user_name>/', views.room_view, name = 'room')
]
