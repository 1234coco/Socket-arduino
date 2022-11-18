
import socket
import time
DNHL = "Đăng nhập hợp lệ"
DNHL = str(DNHL)
Host = "127.168.1.209"
Port = 60432
Format = "utf32"
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print("client side")
s.connect( (Host, Port) )
print("Địa chỉ Client:",s.getsockname())
#gửi
while True:
    A = input(r"Bật hay tắt đèn(BẬT hãy ấn'Y',TẮT bấm bất kỳ phím nào):")
    B = A.encode("utf-32")
    s.sendall(B)


