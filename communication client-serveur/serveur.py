import socketserver
import socket

class HelloTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.request.recv(1024).decode()
        print(f"Le serveur a reçu un message : {msg}")
        self.request.send(f"Le serveur a reçu un message : {msg}".encode())

server = socketserver.ThreadingTCPServer(('127.0.0.1', 3012), HelloTCPHandler) # ThreadingTCPServer
server.serve_forever() # serve forever