from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import json
from ..serveur.backend import School

ip_server = "172.16.16.180"
port = 3080

clients= {}

class EchoWebSocketHandler(WebSocketHandler):
    def open(self):
        """To do when a client connects on the network
        """
        self.first_msg = False

        
    def on_message(self, message):
        """To do when the server gets a message from a client
        """
        request_type, data = message[0], message[1]
        now = ... # TODO

        if request_type == "occupied":
            room, duration = data[0], data[1]
            school.rooms[room].new_occupation(now, duration)

        elif request_type == "ask_room":
            from_room, criteria = data[0], data[1]
            room, itinerary = school.search_room(now, from_room, criteria)
            answer = json.dumps([room, itinerary]).encode()
            self.write_message(answer)


    def on_close(self):
        """To do when a client leaves the network
        """
        pass


if __name__ == '__main__':
    all_reservations = ... # Get info from oasis
    school = School(all_reservations)
    app = Application([(r'/ws', EchoWebSocketHandler)])
    app.listen(3080)
    IOLoop.instance().start()
