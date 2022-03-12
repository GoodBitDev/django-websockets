import urllib.parse

from channels.db import database_sync_to_async
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser


@database_sync_to_async
def get_user(token: str) -> User:
    auth_service = settings.WEBSOCKET['DEFAULT_AUTHENTICATION_CLASS']
    auth = auth_service()
    return auth.get_user(auth.get_validated_token(token))


class TokenAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        params = urllib.parse.parse_qs(scope['query_string'].decode())
        token = None
        try:
            token = params.get('token')[0]
        except KeyError:
            pass

        if token:
            scope['user'] = await get_user(token)
        else:
            scope['user'] = AnonymousUser()
        return await self.app(scope, receive, send)
