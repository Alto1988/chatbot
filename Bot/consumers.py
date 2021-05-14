import json
from channels.generic.websocket import WebsocketConsumer

# this is kind of like rendering a view


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass
# this function loads a message from json and then sends the message off.

    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({'message': message}))
