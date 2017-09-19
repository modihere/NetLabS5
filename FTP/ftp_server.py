import socket

HOST = 'localhost'
PORT = 8009
OUTPUT_FILE = "/home/admin-it/hackrush/FTP/files/up_file.wma"

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.bind((HOST, PORT))

_socket.listen(1)

print ("Server is ready")
com, addr = _socket.accept()

counter = 1
file_name = "file_recv.wma"
f = open(OUTPUT_FILE, 'wb')

while 1:
    recv_file = com.recv(1024)

    while recv_file:
        f.write(recv_file)
        recv_file = com.recv(1024)
        
    break

f.close()
com.close()
_socket.close()

