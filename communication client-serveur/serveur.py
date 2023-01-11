import socketserver
import socket

server_ip = "127.0.0.1"
server_port = 3012

class HelloTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        BUFFER = 1024
        #request_type, data = self.request.recv(BUFFER).decode().split(',')
        #if request_type == "reservations":
        #    self.request.send("Reservations of the day".encode())
        #elif request_type == "free_room":
        #    self.request.send("room,itinerary".encode())
        msg = self.request.recv(BUFFER).decode()
        print(f"Le serveur a reçu un message : {msg}")
        self.request.send(f"Le serveur a reçu un message : {msg}".encode())

server = socketserver.ThreadingTCPServer((server_ip, server_port), HelloTCPHandler) # ThreadingTCPServer
server.serve_forever() # serve forever