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
            return self.reservations[0]['from']
        except:
            return None
    
    def is_booked(self, now, duration):
        next_available = self.get_next_available()
        return ((next_available - now[1] - duration) >= 0)
    
    def is_occupied(self, now, duration):
        if self.occupation == None:
            return False
        else:
            return (now < self.occupation[1]) | (now + duration > self.occupation[0])
    
    def is_available(self, now, duration):
        # Par défaut, on ne propose pas de salle à moins de 10 minutes avant la prochaine réservation
        return ~(self.is_booked(now, duration) | self.is_occupied(now, duration))
    
    def send_reservations(self):
        self.client.write_message(json.dumps({"requête": "edt", "réservations": self.reservations}))