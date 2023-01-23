from .room import Room
from .scrap_oasis import scrap
import json

class School:
    def __init__(self):
        self.rooms:dict[str, Room] = {}
    
    def new_room(self, room_id, client):
        self.rooms[room_id] = Room(room_id, client)
    
    def search_room(self, now, data):
        """Retourne la salle la plus proche, libre, selon certains critères optionnels.
        La liste des priorités a été stockée dans priorityLists.txt, cf. README.md"""
        #TODO
        from_room = data["id"]
        tabb = data["tabb"]
        tabn = data["tabn"]
        videop = data["videop"]
        dur = data["dur"] if data["dur"] != "" else 10 # TODO : add criteria
        with open("room_priorities/priorityLists.txt", 'r') as file:
            priorityList = json.loads(file.read())[from_room]
        for room2go_id in priorityList :
            if self.rooms[room2go_id].is_available(now, dur):
                return room2go_id
        return ""
    
    def update(self):
        """Scraps Oasis and update all rooms"""
        scrap(self.school)