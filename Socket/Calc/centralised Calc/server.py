#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
print s
print 'Calculator server is ready'
print "============================="
conn, addr = s.accept()
print 'connect by', addr

while 1:

	data = conn.recv(50)
	t=data.split(",",3)
	print data
	print t;
	operation=t[0]
	num1= int(t[1])
	num2= int(t[2])
	
	if operation=="add":
		reply=num1+num2
	elif operation=="sub":
		reply=num1-num2
	elif operation=="mul":
		reply=num1*num2
	elif operation=="div":
		reply=num1/num2
	else:
		reply=0

        if not data: break
	print reply
        conn.send(str(reply))
conn.close()
