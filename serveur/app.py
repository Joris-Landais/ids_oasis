from backend import School
from backend.scrap_oasis import update

from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import json

ip_server = "172.16.16.180"
port = 3080

#INITIALIZATION

# Empty school
school = School()

class RoomSocketHandler(WebSocketHandler):
    def open(self):
        self.first_msg = True
    
    def on_message(self, message):
        if self.first_msg:
            # Handle new connection
            self.room_id = message
            self.first_msg = False
            school.new_room(self.room_id, self)
        else:
            request_type = message["requête"]
            now = ... # TODO

            if request_type == "occupied":
                # PAS CLAIR
                duration = message # TODO
                school.rooms[self.room_id].new_occupation(now, duration)

            elif request_type == "recherche de salle":
                room_to_go = school.search_room(now, self.room_id, message) #TODO
                self.write_message(room_to_go)



#LIVE

# Updating and sending their own schedule to each room
update(school)
for room in school.rooms:
    room.send_reservations()

# Request available room
#get info raspberry (room + criteria)
from_room = ...
criteria = ...
now = ...
room_to, itinerary = school.search_room(now, from_room, criteria)
#send to raspebrry available room + itinerary




#CLOSING at the end of the day


# Éteindre les Raspberry ?