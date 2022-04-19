import socket

SERVER_HOST = "localhost" # Establecemos IP del host
SERVER_PORT = 5003        # Establecemos Puerto del host
BUFFER_SIZE = 1024        # Tamaño de datos de ingreso y salida


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos socket (IPv4,TCP)
server.bind((SERVER_HOST, SERVER_PORT))                    # Enlazamos servidor a la IP y puerto

print("Listen in {}:{}".format(SERVER_HOST, SERVER_PORT)) # Inicia la escucha
server.listen(10)                                         # Escucha maxima


server.settimeout(20)                                           # Si pasan 20 segundos de que no se conecto chua socket
client_socket, client_address = server.accept()                 # Acepta conexiones
print(f"{client_address[0]}:{client_address[1]} Connected!")    # Muestra conexion


while True:
    # Envia mensaje
    hello = input("Send a message: ")
    client_socket.send(hello.encode())
    
    # recibe mensaje del servidor dos (como esta en un while pues se solicita denuevo un dato)
    message2 = client_socket.recv(BUFFER_SIZE).decode()
    print(message2)
    
    if hello == "exit" or message2 == "exit":
        break

client_socket.close()
server.close()
