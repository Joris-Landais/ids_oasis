#suggests alternative room if there's an adequate one that's available

#import room's and disponibility's dictionaries and priority list for current room
#files roomDict.py, roomDispo.py and priorityLists.txt should be in the same directory
from roomDispo import dispo
import json

def room2go(now, data) :
    from_room = data["id"]
    with open("priorityLists.txt", 'r') as file:
        priorityList = json.loads(file.read())[from_room]
    room_id = ''
    for room_id in priorityList :
        if dispo[room_id] == 'disponible' : # TODO : change the condition
            return room_id
    return room_id