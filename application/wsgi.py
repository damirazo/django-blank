# coding: utf-8
import os
from django.core.wsgi import get_wsgi_application

__author__ = 'damirazo <me@damirazo.ru>'


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")
application = get_wsgi_application()