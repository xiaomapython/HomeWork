# -*- coding=utf8 -*-

import socket
client = socket.socket()
client.connect(("127.0.0.1", 8000))
print(client)
while True:
    say_to_server = input("Client say:")
    client.sendall(say_to_server.encode())
    if say_to_server == "bye":
        client.close()
        break
    server_reply = client.recv(1024)
    print(server_reply.decode())
