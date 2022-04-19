import socket

SERVER_HOST = "localhost" # IP al cual nos conectaremos
SERVER_PORT = 5003        # Port al cual nos conectaremos
BUFFER_SIZE = 1024        # Tamaño de datos de ingreso y salida

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos socket (IPv4,TCP)
client.connect((SERVER_HOST, SERVER_PORT))                 # Nos conectamos al Host y Puerto 

# Ciclo de mensajeria
while True:
    
    # recibe mensaje
    message1 = client.recv(BUFFER_SIZE).decode()
    print(message1)
    
    # envia mensaje
    message2 = input("Send a another message: ")
    message_send = client.send(message2.encode())
    
    # valida salida
    if message1 == "exit" or message_send == "exit":
           break

# cierra socket de conexion
client.close()
