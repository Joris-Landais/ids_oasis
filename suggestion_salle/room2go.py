#suggests alternative room if there's an adequate one that's available

#import room's and disponibility's dictionaries and priority list for current room
#files roomDict.py, roomDispo.py and priorityLists.txt should be in the same directory
from roomDispo import dispo
import json

def room2go(school, now, data) :
    from_room = data["id"]
    tabb = data["tabb"]
    tabn = data["tabn"]
    videop = data["videop"]
    dur = data["dur"]
    with open("priorityLists.txt", 'r') as file:
        priorityList = json.loads(file.read())[from_room]
    room_id = ''
    for room_id in priorityList :
        if school.rooms[room_id].is_available(now, dur):
            return room_id
    return room_id