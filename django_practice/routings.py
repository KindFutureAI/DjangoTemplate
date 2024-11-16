from django.urls import re_path

from app01 import consumers

websocket_urlpatterns = [
    # 示例 url: ws://127.0.0.1:8000/room/group/
    re_path(r"room/(?P<group>\w+)/$", consumers.ChatConsumer.as_asgi())
]