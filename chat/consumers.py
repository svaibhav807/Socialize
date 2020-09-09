from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message
from django.contrib.auth.models import User
import json

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        user1 = User.objects.get(username = self.user)
        user2 = User.objects.get(username = self.to_chat_user_name)
        messages = Message.objects.filter(author__in=[user1, user2]).order_by('-timestamp')[:10]
        content = {
            'messages': self.messages_to_json(messages)
        }
        self.send_chat_message(content)

    def new_message(self, data):
        author = data['from']
        author_user = User.objects.filter(username=author)[0]
        to_user = User.objects.get(username = data['to'])
        Message.objects.create(author = author_user, content=data['message'], to=to_user)
        message = Message.objects.filter(author = author_user, content = data['message'], to=to_user)
        content = {
            'messages': self.messages_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))

        return result

    def message_to_json(self, message):
        return {
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp),
            'to': message.to.username
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }
    def connect(self):
        self.to_chat_user_name = self.scope['url_route']['kwargs']['user_name']
        self.user = self.scope["user"].username

        to_chat = str(self.to_chat_user_name)
        is_chatting = str(self.user)
        user_list = [to_chat, is_chatting]
        user_list.sort()
        goup_name = user_list[0]+user_list[1]
        self.group_name = goup_name

        self.room_group_name = 'chat_%s' % self.group_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # def send_message(self, message):
    #     self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']

        self.send(text_data = json.dumps(message))



