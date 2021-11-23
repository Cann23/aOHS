import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


# channels layer template
class VideoConsumer2(WebsocketConsumer):
    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            # data to transfer
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            # data to transfer here
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        pass

    # Receive message from room group
    def chat_message(self, event):
        pass


# chat/consumers.py
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        # Join room group
        await self.channel_layer.group_add(
            # data to sent here
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            # data to sent
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        # Send message to room group
        await self.channel_layer.group_send(

        )

    # Receive message from room group
    async def chat_message(self, event):
        pass
