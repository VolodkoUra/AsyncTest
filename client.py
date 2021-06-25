import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

m = ''
while True:
    m = input("Enter message: ")
    if m == "exit":
        break
    clientsocket.send(m.encode())


