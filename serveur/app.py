from backend import School, Room
from backend.scrap_oasis import update

from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop, PeriodicCallback
import json

ip_server = "172.16.16.180"
port = 3080

#INITIALIZATION

# Empty school
global school
school = School()

# REFRESHING AND SENDING
# Only the first room/client will handle the scrapping of Oasis and the send to all other rooms/clients, periodicaly, with a period of refresh_time minutes.
refresh_time = 15 #min
first_client = True #to identify the first client that will have to refresh and send

class RoomSocketHandler(WebSocketHandler):
    def open(self):
        global first_client
        self.first_msg = True
        self.room_id = None #Waiting for the room to send its id
        if first_client:
            # The first client handles refreshing and sending, periodically
            first_client = False
            self.callback = PeriodicCallback(self.refresh, refresh_time * 60000)
    
    def send_updates(self):
        """Sending Oasis updates to the client, every refresh_time minutes.
        """
        school.update()
        for room in school.rooms.values():
            room.send_reservations()
    
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