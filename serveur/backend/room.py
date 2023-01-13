from operator import itemgetter

class Room:
    def __init__(self, room_id:str, week_reservations:list[dict]) :
        self.room_id = room_id
        self.reservations = sorted(week_reservations, key=itemgetter('day', 'from'))
        self.occupation = None

    def new_reservation(self, data_sent:dict):
        self.reservations.append(data_sent)
        self.reservations = sorted(self.reservations, key=itemgetter('day', 'from'))
    
    def new_occupation(self, now, duration:int):
        self.occupation = [now, now + duration]

    def cancel_reservation(self, data_sent:dict):
        # TODO
        self.reservations # TODO
    
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