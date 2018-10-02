# import socket module
from socket import *
from threading import Thread

def deal(connectionSocket,addr):
    try:
        message = connectionSocket.recv(1024)  # 获取客户发送的报文
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read();
        # Send one HTTP header line into socket
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (
            len(outputdata))
        connectionSocket.send(header.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        header = ' HTTP/1.1 404 Found'
        connectionSocket.send(header.encode())
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind(('', 6789))  # 将TCP欢迎套接字绑定到指定端口
serverSocket.listen(5)  # 最大连接数为1

while True:
    # Establish the connection
    try:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # 接收到客户连接请求后，建立新的TCP连接套接字
        print("From [%s] " % str(addr))
        client = Thread(target=deal, args=(connectionSocket, addr))
        client.start()
    except:
        print("error")
serverSocket.close()