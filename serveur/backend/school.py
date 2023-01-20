from .room import Room
from ...suggestion_salle.room2go import room2go
from .scrap_oasis import scrap

class School:
    def __init__(self):
        self.rooms:dict[str, Room] = {}
    
    def new_room(self, room_id, client):
        self.rooms[room_id] = Room(room_id, client)
    
    def search_room(self, now, data):
        room_to_go = room2go(self, now, data)
        return room_to_go
    
    def update(self):
        """Scraps Oasis and update all rooms"""
        scrap(self.school)