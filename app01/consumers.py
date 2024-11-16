# from channels.generic.websocket import WebsocketConsumer
# from channels.exceptions import StopConsumer


# class ChatConsumer(WebsocketConsumer):  # 继承WebsocketConsumer
#    def websocket_connect(self, message):
#         print("有人进行连接了。。。。")
#         # 有客户端向后端发送 WebSocket 连接的请求时，自动触发(握手)
#         self.accept()

#    def websocket_receive(self, message):
#         # 浏览器基于 WebSocket 向后端发送数据，自动触发接收消息
#         print(message)

#         text = message["text"]
#         print("接收到的消息为:", text)
#         self.send("不要回复不要回复！！！")

#    def websocket_disconnect(self, message):
#         # 客户端向服务端断开连接时，自动触发
#         print("连接断开！！")
#         raise StopConsumer()

# ——————————————————————————————————————————————————————
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):  # 继承WebsocketConsumer
    def websocket_connect(self, message):
        # 接收客户端的连接
        self.accept()
        print("连接成功！！！")
        # 获取群号
        print(self.scope["url_route"])
        print(self.scope["url_route"]["kwargs"])
        group_num = self.scope["url_route"]["kwargs"].get("group")
        print("group_num", group_num)

        # 将这个客户端的链接对象添加到某个地方（内存或者 redis）
        # self.channel_layer.group_add(group_num, self.channel_name)
        async_to_sync(self.channel_layer.group_add)(group_num, self.channel_name)


    def websocket_receive(self, message):
        # 浏览器基于 WebSocket 向后端发送数据，自动触发接收消息
        text = message["text"]
        print("接收到的消息为:", text)
        group_num = self.scope["url_route"]["kwargs"].get("group")
        print("group_num", group_num)
        # 通知组内的所有的客户端，执行 xx_oo方法，在方法中可以自定义任意的功能
        # self.channel_layer.group_send(group_num, {"type": "xx.oo", "message": message})
        async_to_sync(self.channel_layer.group_send)(group_num, {"type": "xx.oo", "message": message})

    def xx_oo(self, event):
        text = event["message"]["text"]
        print("发送的 text：", text)
        self.send(text)  # 给组中的每一个人去发送消息

    def websocket_disconnect(self, message):
        # 客户端向服务端断开连接时，自动触发
        print("断开连接！！！")
        group_num = self.scope["url_route"]["kwargs"].get("group_num")

        # self.channel_layer.group_discard(group_num, self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(group_num, self.channel_name)
        raise StopConsumer()
        
