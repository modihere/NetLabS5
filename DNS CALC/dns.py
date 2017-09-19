import socket

HOST = 'localhost'
PORT = 8005

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.bind((HOST, PORT))
_socket.listen(1)


print ("DNS is ready")
com, addr = _socket.accept()

data = com.recv(15)
data = data.decode("UTF-8")

if data == "test.com":
    com.send(("localhost:8006").encode("UTF-8"))
    print("IP sent\nExiting...")

com.close()
_socket.close()
