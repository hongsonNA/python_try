#!/usr/bin/env python3

import socket
import time
import random
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65435        # Port to listen on (non-privileged ports are > 1023)
server_socket = socket.socket()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('data', data)
            if not data:
                break
            print(data.upper())
            if data.upper() == 'EXIT'.encode('utf-8'):
                conn.close()
                print("Close Connect!")
            conn.sendall(data)
# server_socket.listen(1)
#
# (client_socket, client_address) = server_socket.accept()
#
# while True:
#     client_input = client_socket.recv(1024).upper()
#     print(client_input)
#     if len(client_input) > 4 or len(client_input) < 4:
#         client_socket.send("The length of your messege\nneeds to be 4 chracters.\nI know only 4 commands.\nRAND, TIME, NAME & EXIT.\nThanks.")
#     else:
#         if client_input == 'TIME':
#             client_socket.send(time.strftime("%c"))
#         elif client_input == 'RAND':
#             client_socket.send(str(random.randrange(0, 11)))
#         elif client_input == 'NAME':
#             client_socket.send("My master called me \"Arik\". Funny, ha?")
#         elif client_input == 'EXIT':
#             client_socket.send("Exiting.")
#             break
#         else:
#             client_socket.send("Unknown command")
#
# client_socket.close()
# server_socket.close()