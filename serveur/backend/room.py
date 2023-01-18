from operator import itemgetter
import json

class Room:
    def __init__(self, room_id, client) :
        self.room_id = room_id
        self.client = client
        self.occupation = None

    def update_reservations(self, data:list[dict]):
        self.reservations = data
    
    def new_occupation(self, now, duration:int):
        self.occupation = [now, now + duration]
    
    def get_next_available(self):
        try:
            return (self.reservations[0]['day'], self.reservations[0]['from'])
        except:
            return None
    
    def is_available(self, now, duration):
        next_available = self.get_next_available()
        return ((next_available['from'] - now[1] - duration) >= 0) + (next_available['day'] != now[0])
    
    def is_occupied(self, now, duration):
        return 
    
    def send_reservations(self):
        self.client.write_message(json.dumps(self.reservations))