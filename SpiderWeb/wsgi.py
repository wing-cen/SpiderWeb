"""
WSGI config for SpiderWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import django.core.handlers.wsgi

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpiderWeb.settings")

# application = get_wsgi_application()

sys.path.append(r'C:/Users/Administrator/Desktop/SpiderWeb')
#sys.path.append(r'E:/Project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'SpiderWeb.settings'
application = django.core.handlers.wsgi.WSGIHandler()