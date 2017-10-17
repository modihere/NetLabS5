import socket, sys
from threading import Thread

HOST = "localhost"
PORT = 11256

def send_msg(_socket):
    while True:
        msg = input("\n <you>: ")
        if msg == 'quit':
            _socket.close()
            sys.exit()
        msg = msg.encode('utf-8')
        _socket.send(msg)

def recv_msg(_socket):
    while True:
        stuff = _socket.recv(1024)
        print("<response>: ", stuff.decode('utf-8'))

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.connect((HOST, PORT))
print("Connected to chat")
Thread(target=send_msg, args=(_socket,)).start()
Thread(target=recv_msg, args=(_socket,)).start()
