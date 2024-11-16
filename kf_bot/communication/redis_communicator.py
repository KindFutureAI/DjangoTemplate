# communication/redis_communicator.py
import redis
import json
from .message import Message

class RedisCommunicator:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)
        self.pubsub = self.redis_client.pubsub()

    def send_message(self, sender_id, receiver_id, content):
        message = Message(sender_id, receiver_id, content)
        channel = f"channel_{receiver_id}"
        self.redis_client.publish(channel, message.to_json())

    def subscribe(self, agent_id):
        channel = f"channel_{agent_id}"
        self.pubsub.subscribe(channel)

    def listen(self, callback):
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                message_data = message['data'].decode('utf-8')
                message_obj = Message.from_json(message_data)
                callback(message_obj)

    def unsubscribe(self, agent_id):
        channel = f"channel_{agent_id}"
        self.pubsub.unsubscribe(channel)

    def close(self):
        self.pubsub.close()
        self.redis_client.close()