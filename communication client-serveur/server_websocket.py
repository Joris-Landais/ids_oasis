from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import json

class EchoWebSocketHandler(WebSocketHandler):
    def open(self):
        """To do when a client connects on the network
        """
        pass

        
    def on_message(self, message):
        """To do when the server gets a message from a client
        """
        request_type, data = message[0], message[1]
        if request_type == "occupied":
            pass
        elif request_type == "ask_room":
            itinerary = ""
            room = ""
            answer = json.dumps([room, itinerary]).encode()
            self.write_message(answer)


    def on_close(self):
        """To do when a client leaves the network
        """
        pass


if __name__ == '__main__':
    app = Application([(r'/ws', EchoWebSocketHandler)])
    app.listen(3080)
    IOLoop.instance().start()
