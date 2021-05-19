import socket

s=socket.socket()

s.connect(("192.168.1.37",15555))

print(s.recv(4096).decode("utf-8"))

s.send("Mesaj alındı...".encode("utf-8"))

s.close()
