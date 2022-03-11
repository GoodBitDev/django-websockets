import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from websocket import consumers
from websocket.auth import JWTAuthMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.prod')

django.setup()

paths = [
]

application = ProtocolTypeRouter({
    'websocket': JWTAuthMiddleware(URLRouter(paths))
})
