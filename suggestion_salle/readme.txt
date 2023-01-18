These python scripts were made as part of a project of the discipline "Intelligent and Digital Systems (IDS)" for automatizing the booking of rooms at École de Mines with screens located on each room's door.

These scripts are intented to be in one same folder in a Raspberry Pi that will be attached to the screen corresponding to the current room.

roomDict.py is a simple data base in the form of a Python dictionary, containing all the school's rooms which are possible to book and their relevant characteristics (type, number of places, wing, number and letter).

roomDispo.py is another Python dictionary that contains the information on the availability status of each room. It should be constantly updated by a script that retrieves data from the school's site.

roomPriority.py makes a priority list with the possible alternative rooms for all rooms and save it in priorityLists.txt

priorityLists.txt saves all the priority lists for all rooms.

room2go.py suggests an alternative available room for the user when the current room is already booked. It will return the most covenient room (according to the priority list) which is available (according to the disponibility status dictionary). 