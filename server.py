import socket

events = []

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections
def server():
    while True:
        yield serversocket

        connection, address = serversocket.accept()

        buf = connection.recv(64)

        while len(buf) > 0:
            print(buf)
            buf = connection.recv(64)


def server2():
   while True:
        yield serversocket

        connection, address = serversocket.accept()

        buf = connection.recv(64)

        while len(buf) > 0:
            print(buf)
            buf = connection.recv(64)

g1 = server()
g2 = server2()

stack = [g1,g2]

while True:
    s = stack.pop(0)
    next(s)
    stack.append(s)