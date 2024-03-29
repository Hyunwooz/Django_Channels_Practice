import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room , Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
    	# 파라미터 값으로 채팅 룸을 구별
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # 룸 그룹에 참가
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 룸 그룹 나가기
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 웹소켓으로부터 메세지 받음
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        method = text_data_json['method']
        message = text_data_json['message']
        # 룸 그룹으로 메세지 보냄
        if method == 'join':
            await self.find_room(self.room_name)
            
            room = Room.objects.get(title=self.room_name)
            messages = Message.objects.filter(room=room)
            
            real = await self.messages_to_json(messages)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': real,
                    'status': 'join'
                }
            )
        elif method == 'message':
            room = Room.objects.get(title=self.room_name)
            message = Message.objects.create(content=message,room=room)
            real = await self.message_to_json(message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': real,
                    'status': 'message'
                }
            )

    # 룸 그룹 방을 찾거나 만듬
    async def find_room(self, data):
        room = Room.objects.get_or_create(title=data)
    
    # 룸 그룹으로부터 메세지 받음
    async def chat_message(self, event):
        message = event['message']
        status = event['status']

        # 웹소켓으로 메세지 보냄
        await self.send(text_data=json.dumps({
            'message': message,
            'status': status
        }))
    
    async def messages_to_json(self, messages):
        result = []
        
        for message in messages:
            dict_ = message.__dict__
            data = {
                "content": dict_['content'],
                "created_at": str(dict_['created_at'])
            }
            result.append(data)
        
        return result
    
    async def message_to_json(self, message):
        result = []
        dict_ = message.__dict__
        data = {
            "content": dict_['content'],
            "created_at": str(dict_['created_at'])
        }
        result.append(data)
        return result