from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop

class EchoWebSocketHandler(WebSocketHandler):
    def open(self):
        print("Open connection")
        self.write_message("Welcome")
        
    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("close connection")


if __name__ == '__main__':
    app = Application([(r'/ws', EchoWebSocketHandler)])
    app.listen(3080)
    IOLoop.instance().start()
