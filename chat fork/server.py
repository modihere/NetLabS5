import os
import socket as s

HOST = "localhost"
PORT = 11256
_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
_socket.bind((HOST, PORT))
_socket.listen(4)

dict_of_clients = {}

def shout(data):
  for num in dict_of_clients:
    dict_of_clients[num].send(data)

def handle_client(i, conn, addr):
  while 2:
    data = conn.recv(1024)
    if not data:
      print("Connection broken with client", i)
      conn.close()
      break
      
    shout(data)

def server():
  i = 1;
  while i < 4:
    conn, addr = _socket.accept()
    dict_of_clients[i] = conn
    print(dict_of_clients)
    child_pr = os.fork()
    
    if child_pr == 0:
      print("Connected by client", i, addr)
      handle_client(i, conn, addr)
      break
    else:
      i +=1

if __name__ == "__main__":
  server()
