import socket

SERVER_HOST = "localhost"   # IP al cual nos conectaremos
SERVER_PORT = 5003 # Port al cual nos conectaremos
BUFFER_SIZE = 1024 # Tamaño de datos de ingreso y salida


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos socket (IPv4,TCP)
client.connect((SERVER_HOST, SERVER_PORT)) # Nos conectamos al Host y Puerto 


while True:
    
    select = int(input("[1]Verificar usuario\n[2]Agregar usuario\n... "))
    if select == 1:
        try:# Envio de mensaje
            message = input("CUIL: ").lower() 
            print("\n") 
            client.send(message.encode())

            complete_name = client.recv(BUFFER_SIZE).decode()
            print(complete_name)




        except:
            pass 

    if select == 2:
        with open('personas.json') as file:
            data = json.load(file)
            data.write(f"""
,
    '{number}':[
        {
    'nombre': '{name}',
    'apellido': '{surname}'
        
        }
    ]""")        

    if message == "exit": # Si el mensaje es "exit" sale del blucle
        break

client.close() # Cierra comunicacion