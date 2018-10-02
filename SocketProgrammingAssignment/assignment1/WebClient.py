# import socket module
from socket import *
import sys


if len(sys.argv) != 4:
    print("Usage error")
    print("client.py server_host server_port filename")
else:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    host ,port ,filename = sys.argv[1],int(sys.argv[2]),sys.argv[3]
    serverSocket.bind(("localhost",8001))
    serverSocket.connect((host,port))
    message='GET /'+filename+' HTTP/1.1\r\nHost: '+host+':'+str(port)
    message=str.encode(message)
    serverSocket.sendall(message)
    print(serverSocket.recv(1024))
