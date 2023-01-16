#creates a priority list for alternatives rooms based on the characteristics and the location of the current room

#import dictionary
#file roomDict.py should be in the same directory
from roomDict import rooms

#room corresponding to the current raspberry pi
myroom = "L211"

#create priority list for room
'''
1. type
  if == : ok!
  if != : bigger rooms are still valid but with lower priority 
2. wing
  same wing has priority over different wing
3. floor -- looking only at number we can find the closest room no need to do a separate 
4. number
  priority over floor and number (3 and 4) are decided together with the difference between rooms' numbers
5. aditional letter
  alphabetical order
'''

#get all data of our current room
typeRoom = rooms[myroom]["type"];
peopleRoom = rooms[myroom]["personnes"];
wingRoom = rooms[myroom]["aile"];
numbRoom = rooms[myroom]["numero"];
letterRoom = rooms[myroom]["lettre"];

#print(typeRoom,peopleRoom,wingRoom,numbRoom,letterRoom)

#create list with rooms of same type or different type but bigger
listRooms = list()

for room,infos in rooms.items() :
    if room == myroom :
        continue
    elif infos["type"] == typeRoom :
        listRooms.append(room)
    elif infos["personnes"] >= peopleRoom :
        listRooms.append(room)

#print("list of all rooms:\n",listRooms,"\n\npriority list's length:",len(listRooms),"\n")

#find room with biggest priority from the list
def findRoom(myRoom, dicRooms, listRooms) :
    peopleRoom = dicRooms[myRoom]['personnes']
    wingRoom = dicRooms[myRoom]['aile']
    numbRoom = dicRooms[myRoom]['numero']
    letterRoom = dicRooms[myRoom]['lettre']
    priority = 1000
    for room,infos in dicRooms.items() :
        if not (room in listRooms) : 
            continue
        elif infos['numero'] == numbRoom and infos['aile'] == wingRoom:
            if abs(ord(letterRoom) - ord(infos['lettre'])) < priority :
                priority = abs(ord(letterRoom) - ord(infos['lettre']))
                newRoom = room
        elif infos['aile'] == wingRoom :
            if abs(numbRoom - infos['numero']) < priority :
                priority = abs(numbRoom - infos['numero'])
                newRoom = room
        #the next else represents rooms that are in differents wings of the building
        #we add 500 to their priority to make sure that they will never have a bigger priority than a room in the same wing
        else : 
            if abs(numbRoom - infos['numero']) + 500 < priority :
                priority = abs(numbRoom - infos['numero']) + 500
                newRoom = room
    return newRoom

#print(findRoom(myroom, rooms, listRooms))

#make the priority list (first entries have higher priority)
priorityList = list()
for room in rooms :
    if len(listRooms) == 0 :
        break
    newroom = findRoom(myroom,rooms,listRooms) 
    if newroom in listRooms :
        priorityList.append(newroom)
        listRooms.remove(newroom)

#print("priority list:\n",priorityList,"\n\npriority list's length:",len(priorityList),"\n")