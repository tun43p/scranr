import socket

ip = input("Enter an IP address : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(1, 100):
    if sock.connect_ex((ip, i)):
        print(i, " : CLOSED")
    else:
        print(i, " : OPEN")
