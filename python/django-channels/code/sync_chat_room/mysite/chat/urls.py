# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^(?P<room_name>\w+)/$', views.room, name='room')
]
