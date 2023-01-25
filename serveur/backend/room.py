from operator import itemgetter
import json
from datetime import datetime, timedelta

class Room:
    def __init__(self, room_id, client) :
        self.room_id = room_id
        self.client = client
        self.occupation = None

    def update_reservations(self, data:list[dict]):
        self.reservations = data
    
    def new_occupation(self, now:datetime, duration:int):
        self.occupation = [now, now + timedelta(minutes=duration)]
    
    def get_next_available(self):
        try:
            now = datetime.now()
            return datetime(
                year=now.year,
                month = now.month,
                day = now.day,
                hour = int(self.reservations[0]['from_'][:2]),
                minutes = int(self.reservations[0]['from_'][3:])
                )
        except:
            return None
    
    def is_booked(self, now, duration):
        next_available = self.get_next_available()
        return next_available >= now + timedelta(minutes=duration)
    
    def is_occupied(self, now, duration):
        if self.occupation == None:
            return False
        else:
            return (now < self.occupation[1]) | (now + timedelta(minutes=duration) > self.occupation[0])
    
    def is_available(self, now, duration):
        # Par défaut, on ne propose pas de salle à moins de 10 minutes avant la prochaine réservation
        return ~(self.is_booked(now, duration) | self.is_occupied(now, duration))
    
    def send_reservations(self):
        self.client.write_message(json.dumps({"requête": "edt", "réservations": self.reservations}))