#!/usr/bin/env python3
import socket
import time

# class ClintSocket:
#     def __init__(self):
#         self.sendMessage()
#
#     def sendMessage(self):
HOST = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 65435  # The port used by the server
# return HOST
message = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while True:
    message = input("Insert Command\n")
    message = message.encode('utf-8')
    s.sendall(message)
    if message.upper() == 'EXIT':
        break
    message = ''
    # data = s.recv(1024)
print("Application exit!")
    # sendMessage()

# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65433        # The port used by the server
#
# message = ''
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# while True:
#     message = input("Insert Command\n")
#     message = message.encode('utf-8')
#     s.sendall(message)
#     if message.upper() == 'EXIT':
#         break
#     message = ''
#     # data = s.recv(1024)
# print("Application exit!")
# print('Received', repr(data))
