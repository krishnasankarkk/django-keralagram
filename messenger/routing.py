from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:login_user_id>/<str:chat_user_id>/', consumers.ChatConsumer.as_asgi()),
]