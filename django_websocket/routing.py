import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from django_websocket import consumers
from django_websocket.auth import JWTAuthMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.prod')

django.setup()

paths = [
]

application = ProtocolTypeRouter({
    'websocket': JWTAuthMiddleware(URLRouter(paths))
})
