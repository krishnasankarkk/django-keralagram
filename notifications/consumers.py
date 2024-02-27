from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Notification

class NotificationConsumer(AsyncWebsocketConsumer):
    """Consumer to handle notifications."""
    async def connect(self):
        await self.accept()
        
    async def disconnect(self, code):
        pass
    
    async def receive(self, text_data=None, bytes_data=None):
        notifications = Notification.objects.all()
        await self.send({'notifications':notifications})