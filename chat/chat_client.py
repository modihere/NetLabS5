import socket as s

HOST = "localhost"
PORT = 12345
_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
_socket.connect((HOST, PORT))

msg = input("Client's msg: ")
_socket.send(msg.encode('UTF-8'))

while 1:
  data = _socket.recv(12)
  data = data.decode('UTF-8')
  
  if data == 'Bye':
    _socket.send('Bye'.encode('UTF-8'))
    break
  print("Server's msg: ", data)
  msg = input("Client's msg: ")
  _socket.send(msg.encode('UTF-8'))

_socket.close()

