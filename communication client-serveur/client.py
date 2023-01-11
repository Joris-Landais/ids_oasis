import socket
import json
import time

server_ip = "127.0.0.1"
server_port = 3012

params = (server_ip, server_port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(params)

#s.send("Hello Joris".encode())
#msg = s.recv(1024)
#print(f"Le client a reçu '{msg.decode()}'")


BUFFER = 1024

def ask_reservations():
    # Asking for day reservations
    s.send("reservations,haha".encode())
    reservations = s.recv(BUFFER).decode()
    print(f"Reservations : {reservations}")

#def ask_free_room():
    # Asking for nearest room
#    s.send("free_room,Nearest room?".encode())
#    room = s.recv(BUFFER).decode()
#    print(room)
#    #print(itinerary)

ask_reservations()
time.sleep(5)
ask_reservations()
#ask_reservations()