# communication/redis_communicator.py
import redis
import json
from .message import Message

class RedisCommunicator:
    """ RedisCommunicator class for managing communication with Redis. """
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

        # 说明：订阅频道。详细说明：pub/sub 模式, 
        # 是订阅发布模式的一种，它允许客户端订阅一个或多个频道，
        # 当有消息发布到该频道时，所有订阅该频道的客户端都会收到该消息。
        self.pubsub = self.redis_client.pubsub()

    def send_message(self, sender_id, receiver_id, content):
        """ Send a message to the specified receiver. """
        message = Message(sender_id, receiver_id, content)
        channel = f"channel_{receiver_id}"

        # 发布消息：将指定的频道作为键，消息作为值，发布到 Redis 服务器。
        self.redis_client.publish(channel, message.to_json())

    def subscribe(self, agent_id):
        """ Subscribe to a specific agent's channel. """
        channel = f"channel_{agent_id}"

        # 订阅频道：订阅指定频道的消息。
        self.pubsub.subscribe(channel)

    def listen(self, callback):
        """ Listen for incoming messages and call the specified callback function. """
        for message in self.pubsub.listen():

            # message['type'] 是一个字符串，表示消息的类型，可以是 'subscribe'、'unsubscribe'、'message' 等。]
            if message['type'] == 'message': 

                # 'data' 是一个字节串，表示实际的消息数据。
                message_data = message['data'].decode('utf-8')
                message_obj = Message.from_json(message_data)

                # 调用回调函数，将 message_obj 传递给它，以实现消息处理。
                callback(message_obj)

    def unsubscribe(self, agent_id):
        """ Unsubscribe from a specific agent's channel. """
        channel = f"channel_{agent_id}"
        self.pubsub.unsubscribe(channel)

    def close(self):
        """ Close the Redis connection. """
        self.pubsub.close()
        self.redis_client.close()