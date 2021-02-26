# auth/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/home_feed/chat/<str:room_name>/', consumers.ChatConsumer),
]
