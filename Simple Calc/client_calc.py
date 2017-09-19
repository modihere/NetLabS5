import socket as s

HOST = "localhost"
PORT = 11256
_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
_socket.connect((HOST, PORT))

num1 = input("Enter first number ")
num2 = input("Enter second number ")
op = input("Enter operator ")

evalStr = num1 + " " + op + " " + num2

print(evalStr.encode('utf-8'))
_socket.send(evalStr.rstrip().encode('utf-8'))

data = _socket.recv(1042)
_socket.close()
print(evalStr, "is", data.decode('utf-8'))

