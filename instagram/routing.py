from django.urls import path

from messenger.consumers import ChatConsumer
from users.consumers import OnlineStatusConsumer
from notifications.consumers import NotificationConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:login_user_id>/<str:chat_user_id>/', ChatConsumer.as_asgi()),
    path('ws/online/', OnlineStatusConsumer.as_asgi()),
    path('ws/notifications/', NotificationConsumer.as_asgi()),
]