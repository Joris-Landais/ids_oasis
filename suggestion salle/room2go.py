#suggests alternative room if there's an adequate one that's available

#import room's and disponibility's dictionaries and priority list for current room
#files roomDict.py, roomDispo.py and roomPriority.py should be in the same directory
from roomDispo import dispo
from roomPriority import priorityList

def room2go(dispoDict,priList) :
    newRoom = ''
    for room in priorityList :
        if dispo[room] == 'disponible' :
            return room
    return newRoom

def messageOnScreen() :
    newRoom = room2go(dispo,priorityList)
    if newRoom == '' :
        return "Aucune salle disponible correspond aux characteristiques requises"
    else :
        return "Allez à la salle " + newRoom

print(messageOnScreen())