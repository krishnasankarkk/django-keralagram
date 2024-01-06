from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

from .models import UserAccount

class OnlineStatusConsumer(AsyncWebsocketConsumer):
    """Consumer to check user online status."""
    async def connect(self):
        self.user = self.scope["user"]
        await self.accept()
        await self.update_user_status(True)
        
    async def disconnect(self, code):
        await self.update_user_status(False)
        
    @database_sync_to_async
    def update_user_status(self, is_online):
        if self.user.is_authenticated:
            user = UserAccount.objects.get(user_id=self.user.id)
            user.is_online = is_online
            user.update_last_seen()
            