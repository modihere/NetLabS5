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

while True:
  data = conn.recv(1024)

  abc = data.splitlines()
  print(abc[0])
  num1, op, num2 = data.decode('utf-8').split(" ")
  opString = num1 + op + num2

  result = eval(opString)
  result = str(result)

  if not data: break
  conn.send(result.encode('utf-8'))

conn.close()

