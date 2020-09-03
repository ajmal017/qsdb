import json,asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from plotter.services import *


class PlotterConsumer(AsyncWebsocketConsumer):
        
    async def connect(self):
        self.stock_name = self.scope['url_route']['kwargs']['stock_name']
        self.stock_group_name = 'stock_%s' % self.stock_name      
        await self.channel_layer.group_add(
            self.stock_group_name,
            self.channel_name
        )
        self.ib = await connectToIB()
        await self.accept()

    async def disconnect(self, close_code):
        await disconnect_to_ib(self.ib)
        await self.channel_layer.group_discard(
            self.stock_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        await self.channel_layer.group_send(
            self.stock_group_name,
            {
                'type': 'price',
                'message': message
            }
        )

    async def price(self, event):
        message = await requestTick(self.ib)
        await self.send(text_data=json.dumps({
            'message': message
        }))