"""
WSGI config for web_sql_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/lava/Work/web_sql_django/web_sql_proj/')
sys.path.append('/home/lava/Work/web_sql_django/web_sql_proj/web_sql_proj/')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_sql_proj.settings')

application = get_wsgi_application()
