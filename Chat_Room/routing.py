from django.urls import re_path
from . import consumers
from django.urls import re_path
websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<user>\w+)/(?P<room_name>\w+)/$',consumers.ChatRoomConsumer.as_asgi()),
]