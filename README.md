FreeChat
========
This is an easy chat, powered by Django and Tornado

To run this project, please, run "run.py"
It downloads Django, Tornado, creating database and running this two servers in two different threads.

To start using chat open http://localhost:8000/ or link, written in console log.
To Sign Up or Sign in jast tape your username and password. After first authentication, use the same password to Sign In.

Django is used to return pages (page) and ru this website.
Tornado ued for asunc. connection, which is requared to use WebSockets.

 Uncaught InvalidStateError: Failed to execute 'send' on 'WebSocket': already in CONNECTING state. script.js:60
 Means, that tornado server is not actually running on your computer.