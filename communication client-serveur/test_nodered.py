from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop

ip_server = "172.16.16.180"
port = 3080


class EchoWebSocketHandler(WebSocketHandler):
    def open(self):
        print("hello")

        
    def on_message(self, message):
        print("message reçu")
        print(message)
        self.write_message("hello lucie")


    def on_close(self):
        """To do when a client leaves the network
        """
        print("bye-bye")


if __name__ == '__main__':
    app = Application([(r'/ws', EchoWebSocketHandler)])
    app.listen(port, ip_server)
    IOLoop.instance().start()
