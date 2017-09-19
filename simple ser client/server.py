import socket as s

HOST = "localhost"
PORT = 11256
_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
_socket.bind((HOST, PORT))
_socket.listen(1)

print(_socket)
print("Server Ready")

conn, addr = _socket.accept()
print("Connected by", addr, conn)

while 1:
  data = conn.recv(12)
  if not data: break
  conn.send(data)

conn.close()
