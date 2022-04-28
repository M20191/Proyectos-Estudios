import socket
import json

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
    message = client_socket.recv(BUFFER_SIZE).decode() # Recibe mensaje
    
    try:

        # Prosesamiento de datos
    
        with open('personas.json') as file:
            data = json.load(file)
            name = data[message][0]["nombre"]
            surname = data[message][0]["apellido"]

            complete_name = name + " " + surname

            

    except:
        print(f"[LOG] El cuil {message} ingresado no es valido")
        complete_name = "CUIL INVALIDO INGRESE NUEVAMENTE"

    client_socket.send(complete_name.encode())

    # Validacion de salida
    if message == "exit":
        break

# Se cierra conexion y socket        
client_socket.close()
server.close()