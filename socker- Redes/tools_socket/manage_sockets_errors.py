import socket
import sys
host = ""
port = 0

try:
    mysocket = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
    print(mysocket)
    mysocket.settimeout(5)
except socket.error as e:
    print("socket create error: %s" % srt(e.__class__))
    sys.exit(1)

try:
    mysocket.connect((host, port))
    print(mysocket)
except socket.timeout as e:
    print("Timeout %s" % e)
except socket.gaierror as e:
    print("Connection error to the server:%s" % s)
except socket.error as e:
    print("Connection error: %s" % e)
    sys.exit(1)