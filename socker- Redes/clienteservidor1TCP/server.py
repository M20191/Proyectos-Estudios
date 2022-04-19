import socket

SERVER_HOST = "localhost"   # Establecemos IP del host
SERVER_PORT = 5003          # Establecemos Puerto del host
BUFFER_SIZE = 1024          # Tamaño de datos de ingreso y salida


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos socket (IPv4,TCP)
server.bind((SERVER_HOST, SERVER_PORT)) # Enlazamos servidor a la IP y puerto

print("Listen in {}:{}".format(SERVER_HOST, SERVER_PORT)) # Inicia la escucha
server.listen(10)                                         # Escucha maxima

client_socket, client_address = server.accept() # Acepta conexiones
print(f"{client_address[0]}:{client_address[1]} Connected!") # Muestra conexion

while True:

    # Envio de mensaje
    message = input("Send a msg:").lower() 
    print("Message sent") 
    client_socket.send(message.encode())

    # Validacion de salida
    if message == "exit":
        break

# Se cierra conexion y socket        
client_socket.close()
server.close()
