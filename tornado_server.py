import json
import datetime
import logging
from tornado.web import Application
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from FreeChat.settings import DEFAULT_TORNADO_PORT

#List of all connected clients
clients = []


class WebSocketChatHandler(WebSocketHandler):
    def open(self, *args):
        """Invoked when a new WebSocket is opened."""
        clients.append(self)  #Adding new connected client to the global list

    def on_message(self, message):
        """Handle incoming messages on the WebSocket"""
        d = datetime.datetime.now()  #Time, when message was handled
        m = json.loads(message)  #Parsing of JSON mesage
        logging.info(u'User [%s] sent a message "%s"' % (m["username"], m["message"]))
        m["date"] = d.isoformat()  #Adding current time
        for client in clients:  #resending message to all connected clients
            client.write_message(message)

    def on_close(self):
        """Invoked when the WebSocket is closed."""
        clients.remove(self)  #Removing disconnected client from the global list


def initialize_logger():
    """Initializing parameters for logger, to log to file and concole
    at the same time """
    logger = logging.getLogger()
    formatter = logging.Formatter("# %(levelname)-4s [%(asctime)s]  %(message)s")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)
    handler = logging.FileHandler("messages.log", "w")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


initialize_logger()

app = Application([(r'/chat', WebSocketChatHandler)])
app.listen(DEFAULT_TORNADO_PORT)
IOLoop.instance().start()