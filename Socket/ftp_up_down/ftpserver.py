import socket

HOST = 'localhost'
PORT = 5009

s = socket.socket()
s.bind(('', PORT))
s.listen(2)
print s
print 'FTP Server is ready....!!!'
print 'you can upload/download a file.'
print "please be carefull writting filename, it is case sensetive.."
print"==============================================================="
conn,addr=s.accept()
print 'connect by',addr,conn
         
while (1):
	data=conn.recv(1024)
	if not data: break
	l=data.split()
	print'processing please wait.....'
	if l[0]=='download':
		f=open("bb1.mpeg","rb")
		l=f.read(1024)
		while(l):
			conn.send(l)
			l=f.read(1024)
			if len(l)==0:
				break	
		
		print'file sent successful..'
		f.close()
		print "FTP Server: bye.."
		
	else:
		#server side upload code
		f=open("up.mpeg","wb")
		p=conn.recv(1024)
		while(p):
			f.write(p)
			p=conn.recv(1024)
			if p=='' or p == 'END OF SERVICE':
				f.close()	

		print'file received successful..'
		
		print "FTP Server: bye.."
	s.close()
