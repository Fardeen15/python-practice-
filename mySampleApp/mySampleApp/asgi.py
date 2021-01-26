"""
ASGI config for mySampleApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

from whitenoise.django import DjangoWhiteNoise
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySampleApp.settings')

application = get_asgi_application()
application = DjangoWhiteNoise(application)
