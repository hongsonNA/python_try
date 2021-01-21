#!/usr/bin/env python3

import socket
from clientThread import ClientThread
import time
import random
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
client = []
server_socket = socket.socket()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(4)
    print('Start listening...')
    conn, addr = s.accept()
    with conn:
        while True:
            print('Connected by', addr)
            client.append(ClientThread(conn, addr, client))
            client[-1].start()
            data = conn.recv(1024)
            print('data', data)
            if not data:
                break
            print(data.upper())
            if data.upper() == 'EXIT'.encode('utf-8'):
                conn.close()
                print("Close Connect!")
            conn.sendall(data)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(4)
#     print('Server is listening...')
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             try:
#                 print('Connected by', addr)
#                 client.append(ClientThread(conn, addr, client))
#                 client[-1].start()
#             except Exception as e:
#                 print(e)