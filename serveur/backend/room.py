from operator import itemgetter

class Room:
    def __init__(self, room_id:str, week_reservations:list[dict]) :
        self.room_id = room_id
        self.reservations = sorted(week_reservations, key=itemgetter('day', 'from'))
        self.currently_booked = False
        self.currently_occupied = False
        try:
            self.next_booking = (self.reservations[0]['day'], self.reservations[0]['from'])
        except:
            self.next_booking = None

    def new_reservation(self, data_sent:dict):
        self.reservations.append(data_sent)
        self.reservations = sorted(self.reservations, key=itemgetter('day', 'from')) 

    def cancel_reservation(self, data_sent:dict):
        # TODO
        self.reservations # TODO