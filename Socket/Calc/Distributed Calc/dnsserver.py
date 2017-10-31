import socket

HOST = 'localhost'
PORT = 5021
s = socket.socket()
s.bind(('', PORT))
s.listen(2)
print s
print 'DNS Server is ready....!!!'
print 'You can request for calculation..'

print"==============================================================="
conn,addr=s.accept()
print 'connect by',addr,conn
result=''
while (1):
	data=conn.recv(1024)
	if not data: break
	print "i received ",data
	l=data.split("#",3)
	operation=l[0]
	if operation=="+":
		
		HOST = 'localhost'
		PORT = 5022
		s1 = socket.socket()
		s1.connect((HOST, PORT))
		s1.send(data)
		result=s1.recv(1024)
		print "result= ", result
		s1.close();
	elif operation=="-":
		
		HOST = 'localhost'
		PORT = 5023
		s1 = socket.socket()
		s1.connect((HOST, PORT))
		s1.send(data)
		result=s1.recv(1024)
		print "result= ", result
		s1.close();
	elif operation=="*":
		
		HOST = 'localhost'
		PORT = 5024
		s1 = socket.socket()
		s1.connect((HOST, PORT))
		s1.send(data)
		result=s1.recv(1024)
		print "result= ", result
		s1.close();
	elif operation=="/":
		
		HOST = 'localhost'
		PORT = 5025
		s1 = socket.socket()
		s1.connect((HOST, PORT))
		s1.send(data)
		result=s1.recv(1024)
		print "result= ", result
		s1.close();
	else:
		print"Quit.. not a valid operation."
	conn.send(result)
s.close()
