import socket

s = socket.socket()
host = '127.0.0.1'
port = 8888
byte_message = bytes("hello world!", "utf-8")
s.connect((host, port))
s.sendto(byte_message, (host, port))
message = s.recv(256)
print(bytes.decode(message, 'utf-8'))
s.close()
