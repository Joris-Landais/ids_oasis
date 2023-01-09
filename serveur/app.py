from backend import School



#INITIALIZATION

# Getting reservation from OASIS
all_reservations = ...


# Initializing all the rooms
school = School(all_reservations=all_reservations)



# Sending their own schedule to each room





#LIVE

# New reservation
data_new_reservation = ...
room_id = ...
school.rooms[room_id].new_reservation(data_new_reservation)
# + envoi raspberry

# Cancel reservation
data_cancel_reservation = ...
room_id = ...
school.rooms[room_id].cancel_reservation(data_cancel_reservation)
#+envoi raspberry


# Request available room
#get info raspberry (room + criteria)
from_room = ...
criteria = ...
room_to, itinerary = school.search_room(from_room, criteria)
#send to raspebrry available room + itinerary




#CLOSING at the end of the day
