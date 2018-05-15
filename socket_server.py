# -*- coding=utf8 -*-
import socket
server = socket.socket()  # 默认tcp

# 可以修改为UDP协议
# server = socket.socket(socket.SOCK_DGRAM)

server.bind(("127.0.0.1", 8000))
server.listen()
flag = True
while flag:
    conn, address = server.accept()
    while flag:
        try:
            msg = conn.recv(1024).decode()
            print("{} say:".format(address[0]), msg)
            conn.sendall("收到".encode())
        except OSError as e:
            conn.close()
            print("客户端自动断开连接")
            flag = False
