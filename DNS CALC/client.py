import socket

HOST = 'localhost'
PORT = 8005

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.connect((HOST, PORT))

site = "test.com"

_socket.send((site.encode("UTF-8")))

ans = _socket.recv(20)
ans = ans.decode('UTF-8')

print ("IP is: ", ans)
_socket.close()

print("Type \"Exit\" to exit the calculator")
HOST, PORT = ans.split(":")

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.connect((HOST, int(PORT)))

while 1:
    imp = input("\nEnter Input: ")

    if imp.lower() == "exit":
        break

    _socket.send((imp.encode("UTF-8")))
    ans = _socket.recv(15)
    ans = ans.decode('UTF-8')
    print ("Answer Is: ", ans)

_socket.close()
