A = 0
import socket
import time
import serial



Host = "127.168.1.209"
Port = 60432
Format = "utf32"
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen()
print("server side")
print("server:", Host, Port)
print("chờ")
conn, addr = s.accept()
print("clint address:", addr)
print("conn:",conn.getsockname())
GS = serial.Serial('com6',9600)

while True:
    C = conn.recv(50).decode("utf-32")
    C = C.encode()
    GS.write(C)

    

