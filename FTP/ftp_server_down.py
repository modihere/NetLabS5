import socket

HOST = 'localhost'
PORT = 8009
INPUT_FILE = "/home/admin-it/hackrush/FTP/files/file.wma"

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.bind((HOST, PORT))

_socket.listen(1)

print ("Server is ready")
com, addr = _socket.accept()

f = open(INPUT_FILE, 'rb')
send_file = f.read(1024)

while send_file:
    com.send(send_file)
    send_file = f.read(1024)

f.close()
com.close()
_socket.close()

