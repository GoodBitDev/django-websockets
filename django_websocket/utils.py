from django.conf import settings
import importlib


def get_auth_service_class():
    auth_service_path = settings.WEBSOCKET['DEFAULT_AUTHENTICATION_CLASS'].split('.')
    auth_service_class_name = auth_service_path.pop(-1)

    return getattr(importlib.import_module('.'.join(auth_service_path)), auth_service_class_name)