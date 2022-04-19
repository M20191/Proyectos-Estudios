import socket

SERVER_HOST = "localhost"   # IP al cual nos conectaremos
SERVER_PORT = 5003 # Port al cual nos conectaremos
BUFFER_SIZE = 1024 # Tamaño de datos de ingreso y salida


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos socket (IPv4,TCP)
client.connect((SERVER_HOST, SERVER_PORT)) # Nos conectamos al Host y Puerto 


while True:
    message = client.recv(BUFFER_SIZE).decode() # Recibe mensaje
    print("Server: ", message) # Imprime mensaje por pantalla
    if message == "exit": # Si el mensaje es "exit" sale del blucle
        break

client.close() # Cierra comunicacion
