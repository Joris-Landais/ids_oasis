from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop

ip_server = "172.16.16.180"
port = 3080


class EchoWebSocketHandler(WebSocketHandler):
    def open(self):
        print("nouvelle connection")
        self.first_msg = True # To get room_id

        
    def on_message(self, message):
        if self.first_msg:
            print("premier message reçu")
            print(message)
            self.room_id = message # Saving room_id
            self.first_msg = False
        else:
            print("autre message reçu")
            print(message)
            self.write_message("hello lucie3")


    def on_close(self):
        """To do when a client leaves the network
        """
        print("bye-bye")


if __name__ == '__main__':
    app = Application([(r'/ws', EchoWebSocketHandler)])
    app.listen(port, ip_server)
    IOLoop.instance().start()
