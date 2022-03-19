import base64
import json
import pickle
import socket
import struct

import cv2
from PIL import Image
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # clientı başlat



    def disconnect(self, close_code):
        # client ı bitir
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        HOST = ''
        PORT = 8485

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        s.bind((HOST, PORT))
        print('Socket bind complete')
        s.listen(10)
        print('Socket now listening')

        conn, addr = s.accept()

        data = b""
        payload_size = struct.calcsize(">L")
        print("payload_size: {}".format(payload_size))
        while True:
            while len(data) < payload_size:
                print("Recv: {}".format(len(data)))
                data += conn.recv(4096)

            print("Done Recv: {}".format(len(data)))
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]
            print("msg_size: {}".format(msg_size))
            while len(data) < msg_size:
                data += conn.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            im = Image.fromarray(frame)
            im.save('/home/enssr/Desktop/image.png')
            print(im)
            s = base64.b64encode(im.tobytes())
            # print(s)
            # cv2.imshow('ImageWindow', frame)
            # cv2.waitKey(1)
            self.send(bytes_data=im.tobytes())
            # while True:
            # self.send(text_data=json.dumps({
            #     'message': message
            # }))


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
