import socket

HOST = 'localhost'
PORT = 5021
s = socket.socket()
s.connect((HOST, PORT))

print 'this is client code which will request for operations.'

print"==============================================================="
operation=raw_input('Enter the operation(+ - * /):\n')
a=input("enter 1st operator value: ")
b=input("enter 2nd operator value:")
l=operation+"#"+str(a)+"#"+str(b)
s.send(l)
result=s.recv(1024)
print "Result for operation:",operation
print "result= ",result
s.close()

