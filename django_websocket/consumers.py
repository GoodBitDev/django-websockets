# Contains all websockets consumers
from abc import ABC

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User, AnonymousUser

from django_websocket.signals import S_user_connected_to_websocket, S_user_disconnected_from_websocket


class BaseWebsocketConsumer(WebsocketConsumer, ABC):
    """
    Базовый вебсокет консьюмер.

    Необходимо указать:
        - group_prefix: str - префикc группы, должен быть уникальным для каждого WebsocketConsumer. Например: 'chat'.
        - handler_func_name: str - название функции, которая будет обрабатывать сообщение приходящие в консьюмера
        - url_kwarg_field(optional): str - ключ для получения id группы.
    """

    group_prefix: str
    url_kwarg_field = 'pk'
    handler_func_name: str

    def get_kwarg_from_url(self) -> str:
        return self.scope['url_route']['kwargs'][self.url_kwarg_field]

    def get_group_name(self):
        group_id = self.get_kwarg_from_url()
        return f"{self.group_prefix}_{group_id}"

    def get_user_from_scope(self) -> User:
        try:
            user = self.scope['url_route']['kwargs']['user']
        except KeyError:
            user = AnonymousUser()
        return user

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(self.get_group_name(), self.channel_name)
        S_user_connected_to_websocket.send(sender=self.__class__, user=self.get_user_from_scope(),
                                           channel=self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.get_group_name(), self.channel_name)
        S_user_disconnected_from_websocket.send(sender=self.__class__, user=self.get_user_from_scope(),
                                                channel=self.channel_name)
