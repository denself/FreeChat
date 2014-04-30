"""This is a runfile. It checks, do you have django and tornado
 installed in your machine, and in case o need, it loads them"""

import threading
import os
import socket
import webbrowser
from FreeChat.settings import DEFAULT_DJANGO_PORT

#Checking and downloading tornado
try:
    import tornado
except ImportError:
    os.system('pip install tornado')
#Checking and downloading django
try:
    import django
except ImportError:
    os.system('pip install django')

#Creating database to store users' information
from django.core.management import call_command

os.environ['DJANGO_SETTINGS_MODULE'] = 'FreeChat.settings'
call_command('syncdb', interactive=False)

#Creating of personal thread for django server
run_django = lambda: os.system('python manage.py runserver 0.0.0.0:%s'%DEFAULT_DJANGO_PORT)
djthread = threading.Thread(target=run_django)
djthread.start()
print "To start chat go to http://%s:%s/"%(socket.gethostbyname(socket.gethostname()), DEFAULT_DJANGO_PORT)
#Starting Tornado server
import tornado_server
