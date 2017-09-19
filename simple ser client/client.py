import socket as s

HOST = "localhost"
PORT = 11256
_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
_socket.connect((HOST, PORT))
_socket.send("Hello, World".encode('utf-8'))

data = _socket.recv(12)
_socket.close()
print("Received:", data.decode('utf-8'))

