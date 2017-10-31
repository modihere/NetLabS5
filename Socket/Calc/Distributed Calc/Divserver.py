import socket

HOST = 'localhost'
PORT = 5025
s = socket.socket()
s.bind(('', PORT))
s.listen(2)
print s
print 'Division Server is ready....!!!'
print 'You can request for Division .'

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
	if l[2]==0:
		result="stupid..I cannot divide by zero...I am not Rajnikant.."
	if operation=="/":
		result=str(int(l[1])/int(l[2]))
		print "result= ", result
	
	else:
		result="Quit"
	
	conn.send(result)
s.close()
