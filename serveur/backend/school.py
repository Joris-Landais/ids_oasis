from .room import Room

class School:
    def __init__(self, all_reservations:list[tuple(str, list[dict])]):
        self.rooms = {}
        for room in all_reservations:
            self.rooms[room[0]] = Room(
                room_id=room[0],
                week_reservations=room[1]
            )
    
    def search_room(self, now, from_room:str, criteria:dict):

        itinerary = ...
        room_to = ...
        return room_to, itinerary