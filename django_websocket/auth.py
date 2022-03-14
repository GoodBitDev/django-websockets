import urllib.parse

from channels.db import database_sync_to_async
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from django_websocket.settings import AUTH_SERVICE_CLASS


@database_sync_to_async
def get_user(token: str) -> User:
    auth_service = AUTH_SERVICE_CLASS()
    return auth_service.get_user(auth_service.get_validated_token(token))


class QueryParamTokenAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        params = urllib.parse.parse_qs(scope['query_string'].decode())

        token_param: list = params.get('token', None)
        if token_param:
            user = await get_user(token_param[0])
        else:
            user = AnonymousUser()

        scope['user'] = user
        print(user)
        return await self.app(scope, receive, send)
