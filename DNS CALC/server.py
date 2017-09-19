import socket

HOST = 'localhost'
PORT = 8006

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.bind((HOST, PORT))

_socket.listen(1)

print ("Server is ready")
com, addr = _socket.accept()

while 1:
    data = com.recv(12)
    data = data.decode("UTF-8")

    if not data:
        break

    print ("\nValues received... Calculating.")
    res = eval(data)
    print(" Answer sent...")
    com.send((str(res)).encode("UTF-8"))

com.close()
_socket.close()
