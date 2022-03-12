"""
Приложение для работы с websocket.

В данном модуле идет обработка всех подключений и работы с отправкой данных на каналы или группы,
которые были созданы после подключения пользователей к вебсокету.

websocket/consumers: Содержит все WebSocketConsumer объекты, они обрабатывют подключение
пользователей по websocket.
websocket/routing: Каждому WebSocketConsumer указывается в url путь.
websocket/enums: Содержит все enum нужные для работы самого модуля, и других модулей.
websocket/signals: Содержит/обрабатывает сигналы, которые отправляются/приходят от WebSocketConsumer
"""


from django.apps import AppConfig


class WebsocketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_websocket'

    def ready(self):
        import django_websocket.signals
