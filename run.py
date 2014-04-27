import threading, os, socket
try:
    import tornado
except:
    os.system('pip install tornado')

__author__ = 'denself'
run_django = lambda: os.system('python manage.py runserver 0.0.0.0:8000')
djthread = threading.Thread(target=run_django)
djthread.start()
print "To start chat go to http://"+socket.gethostbyname(socket.gethostname())+":8000/"
print socket.gethostbyname(socket.gethostname())
import app
