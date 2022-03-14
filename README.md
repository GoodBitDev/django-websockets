# Django_Websocket

Библиотека для удобной работы с websocket в django.

## Функции:
- Высокоуровневый сервис для отправки сообщений в вебсокет.
- Консьюмеры, поддерживающие авторизацию клиентского подключения.
- Удобный интерфейс общения с подключенными клиентами.
- Сигналы при подключении к каналу, либо отключении от него.


## Установка:
### PyPI:
```bash
pip install django_websocket
```

### GitHub:
```bash
pip install git+https://github.com/GoodBitDev/django-websockets.git
```


## Использование:

### Consumers:

```python
# consumers.py
import json

#  Импортируем базового консьюмера
from django_websocket.consumers import BaseWebsocketConsumer

# Создадим консьюмера для работы с пользователем
class UserConsumer(BaseWebsocketConsumer):
    # При наследовании необходимо указать:
    group_prefix = 'user'
    handler_func_name = 'base_message'  
    url_kwarg_field = 'user_pk'  
    
    def base_message(self, event):
        data = event['data']
        self.send(text_data=json.dumps(data))
```

BaseWebsocketConsumer - базовый класс, от которого необходимо наследоваться. Дополняет WebSocketConsumer из библиотеки channels.
- group_prefix - prefix группы, которая будет использоваться для общения с клиентом
- handler_func_name - название функции, которая будет обрабатывать сообщения от WebSocketService сервиса(название может быть любое, уникально для каждого консьюмера)
- url_kwarg_field - название параметра в пути запроса, определения подключения


## Авторизация:

Для использования в настройках необходимо указать:


```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

# Импортируем QueryParamTokenAuthMiddleware
from django_websocket.auth import QueryParamTokenAuthMiddleware

# Импортируем консьюмера, который был создан в главе Consumers
from websockets import consumers



paths = [
    path('ws/user/<int:user_pk>', consumers.UserConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': QueryParamTokenAuthMiddleware(URLRouter(paths))
})
```

QueryParamTokenAuthMiddleware - middleware для работы авторизации пользователя по токену указанному в query params, в параметре token.