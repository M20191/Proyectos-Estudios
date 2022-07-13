import socket
import sys

def check_ports(ip,portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print(f"Port {port}: \t Open")
            else:
                print(f"Port {port}: \t Close")
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Connection error")
        sys.exit()
check_ports("0.0.0.0",[443])


