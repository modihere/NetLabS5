import socket

HOST = 'localhost'
PORT = 5009

s = socket.socket()
s.connect((HOST, PORT))
print 'you can upload/download a file.'
print "please be carefull writting filename, it is case sensetive.."
print"==============================================================="
operation=raw_input('Enter the operation(download or upload):\n')
if operation=='upload':

	print'uploading.....'
	f=open("bb1.mpeg","rb")
	l=f.read(1024)

	while(l):
		s.send(l)
		l=f.read(1024)
	
	print'file uploaded successful....'
	f.close()
	

elif operation=='download':
	data=operation
	s.send(data)
	print'downloading.....'
	f=open("down.mpeg","wb")
	l=s.recv(1024)
	size=0
	while(l):
		f.write(l)
		size+=len(l)
		print 'file size= ',size/(1024),'Kilobytes downloaded. still downloading.....'
		l=s.recv(1024)
		if l=='' or l == 'END OF SERVICE':
			break

	print'file size=',size/1024,'KB   downloaded successful...'
	f.close()
	
s.close()

