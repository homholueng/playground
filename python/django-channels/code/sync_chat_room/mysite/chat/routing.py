# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url('ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer)
]
