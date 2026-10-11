import socket

message = ""
while message != "Terminate":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    message = input("Enter horizontal, verical displacement, seperated by spaces (To terminate, enter 'Terminate'):  ")
    client.send(message.encode())
    print(client.recv(1024).decode() + '\n')