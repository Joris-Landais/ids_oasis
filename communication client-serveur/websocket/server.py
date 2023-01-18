from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import json
from ..serveur.backend import School

ip_server = "172.16.16.180"
port = 3080


class Room_Client(WebSocketHandler):
    def open(self):
        """To do when a client connects on the network
        """
        self._first_msg = False

        
    def on_message(self, message):
        """To do when the server gets a message from a client
        """
        if self.first_msg:
            self.room_id = message
            self._first_msg = False
        else:
            request_type, data = message[0], message[1]
            now = ... # TODO

            if request_type == "occupied":
                duration = data[0] # TODO
                school.rooms[self.room_id].new_occupation(now, duration)

            elif request_type == "ask_room":
                criteria = data[0] # TODO
                room, itinerary = school.search_room(now, self.room_id, criteria) #TODO
                answer = json.dumps([room, itinerary]).encode()
                self.write_message(answer)


    def on_close(self):
        """To do when a client leaves the network
        """
        pass


if __name__ == '__main__':
    all_reservations = ... # Get info from oasis
    school = School(all_reservations)
    app = Application([(r'/ws', Room_Client)])
    app.listen(3080)
    IOLoop.instance().start()
