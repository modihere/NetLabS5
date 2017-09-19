import socket as s

HOST = "localhost"
PORT = 12345
_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
_socket.bind((HOST, PORT))
_socket.listen(1)

print(_socket)
print("Server Ready\n")

conn, addr = _socket.accept()

while 1:
  data = conn.recv(12)
  data = data.decode('UTF-8')

  if data == 'Bye':
    conn.send('Bye'.encode('UTF-8'))    
    break
  print("Client's msg: ", data)
  msg = input("Server's msg: ")
  conn.send(msg.encode('UTF-8'))

conn.close()
