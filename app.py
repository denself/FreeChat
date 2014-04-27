from tornado.web import Application
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
import json
import time
clients = []
f = open("log.txt", 'a')


class WebSocketChatHandler(WebSocketHandler):
    def open(self, *args):
        print time.strftime("%c") + " User connected"
        clients.append(self)

    def on_message(self, message):
        m = json.loads(message)
        print m["date"]+" "+m["username"]+" "+m["message"]
        f.write(m["date"]+" "+m["username"]+" "+m["message"]+"\n")
        f.flush()
        for client in clients:
            client.write_message(message)

    def on_close(self):
        print time.strftime("%c") + " User disconected"
        clients.remove(self)


app = Application([(r'/chat', WebSocketChatHandler)])

app.listen(80)
IOLoop.instance().start()