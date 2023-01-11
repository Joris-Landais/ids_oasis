server_ip = "127.0.0.1"
server_port = 3012

import socket

params = (server_ip, server_port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(params)

s.send("Hello Joris".encode())
msg = s.recv(1024)
print(f"Le client a reçu '{msg.decode()}'")