"""
WSGI config for JDemotions project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JDemotions.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

application = get_wsgi_application()
