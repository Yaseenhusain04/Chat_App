from django.urls import path
from .views import register, user_login
from .views import chat_room

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('room/<str:room_name>/', chat_room, name='chat_room'),
]