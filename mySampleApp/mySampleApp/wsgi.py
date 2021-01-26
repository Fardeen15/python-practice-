"""
WSGI config for mySampleApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

# from whitenoise.django import DjangoWhiteNoise
import os
# from whitenoise.django import DjangoWhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySampleApp.settings')

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
