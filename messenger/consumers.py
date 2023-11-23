import json 

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from .models import Message 
from users.models import UserAccount

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_user_id = self.scope["url_route"]["kwargs"]["chat_user_id"]
        self.login_user_id = self.scope["url_route"]["kwargs"]["login_user_id"]
        # Sort user IDs and create a room ID
        sorted_ids = sorted([self.chat_user_id, self.login_user_id])
        room_id = '-'.join(sorted_ids) 
        self.group_name = f"chat_{room_id}"
        #Join room
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

        
    async def disconnect(self, close_code):
        # Leave the group.
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        pass
        
    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        receiver = text_data_json["receiver"]
        sender = text_data_json["sender"]
        from_user = await sync_to_async(User.objects.get)(id=sender)
        from_user_account = await sync_to_async(UserAccount.objects.get)(user_id=sender)
        to_user = await sync_to_async(User.objects.get)(id=receiver)
        to_user_account = await sync_to_async(UserAccount.objects.get)(user_id=receiver)
        new_message = await sync_to_async(Message.objects.create)(
            from_user=from_user, to_user=to_user, message=message
        )
        serialized_message = {
            'type':'chat_message',
            'id': new_message.id,
            'from_user': new_message.from_user.id,
            'to_user': new_message.to_user.id,
            'message': new_message.message,
            'from_user_gender': from_user_account.gender,
            'to_user_gender': to_user_account.gender,
            'created_at': new_message.created_at.isoformat(),
        }
        # send message to group
        await self.channel_layer.group_send(
            self.group_name,
            serialized_message
            # text_data=json.dumps(serialized_message)
        )
    
    async def chat_message(self, new_message):
        serialized_message = {
            'id': new_message['id'],
            'from_user': new_message['from_user'],
            'to_user': new_message['to_user'],
            'from_user_gender': new_message['from_user_gender'],
            'to_user_gender': new_message['to_user_gender'],
            'message': new_message['message'],
            'created_at': new_message['created_at'],
        }
        # Send message to websocket
        await self.send(text_data=json.dumps(serialized_message))
        
        