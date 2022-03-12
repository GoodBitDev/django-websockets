from enum import Enum

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django_websocket.consumers import BaseWebsocketConsumer


class WebSocketService:
    """ Base websocket service """
    @staticmethod
    def _send_to_channel(channel: str, data: dict, handler: str, event_id: int = None):
        """
        Send data to single ws channel

        :param channel: The channel which you want to send the date
        :param data: Data that will be sent to BaseConsumer
        :param handler: Websocket consumer handler
        :param event_id: Event type(optional)
        """
        async_to_sync(get_channel_layer().send)(
            channel,
            {
                'type': handler,
                'event': event_id,
                'data': data,
            }
        )

    @staticmethod
    def _send_to_group(group: str, data: dict, handler: str, event_id: int = None):
        """
        Send data message to ws group

        :param group: Group which you want to send the date
        :param data: Data that will be send to BaseConsumer
        :param event_id: Event type(optional)
        :param handler: Websocket consumer handler
        """
        async_to_sync(get_channel_layer().group_send)(
            group,
            {
                'type': handler,
                'event': event_id,
                'data': data,
            }
        )

    def send_message(self, consumer, data: dict, group: str, event: Enum = None):
        """
        Отправляет сообщение в указанный consumer, который наследуется от GroupWebsocketConsumer.

        :param consumer: WebSocketConsumer в который нужно отправить сообщение.
        :param data: Данные, которые нужно отправить.
        :param group: websocket группа, в которую будет отправлено сообщение.
        :param event: Тип нотификации(optional).
        """

        assert issubclass(consumer, BaseWebsocketConsumer)

        event_id = event.value if event else None
        self._send_to_group(group, data, consumer.handler_func_name, event_id=event_id)

