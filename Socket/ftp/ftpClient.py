import sys
import socket

host="localhost"
port=5003

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print

while(1):
	data=s.recv(1024)
	print data
	choice=raw_input()
	s.send(choice)

	if(choice=="download"):
		data=s.recv(100)
		print data			############################
		while(len(data)!=0):

			data=s.recv(100)
			if (str(data)=="exit"):
				break
			print data

		filename=raw_input("enter filename: ")
		s.send(filename)
		#print "file name sent as ",filename
		filename="downloaded_"+filename
		f1=open(filename,'wb')
		data=s.recv(1024)
		while(data):
			f1.write(data)
			data=s.recv(1024)
			#if(str(data)=="quitt"):
			#	break
			if data=='' or data == 'END OF SERVICE' or data=="quitt":
				break

		f1.close()
		print "check"
		print s.recv(100)

	elif(choice=="upload"):
		data=s.recv(100)
		print data
		filename=raw_input()
		s.send(filename)
		f1=open(filename,'rb')
		l=f1.read(1024)
		while(len(l)!=0):
			s.send(l)
			l=f1.read(1024)
		s.send("file uploaded successfully\n")
	
	elif(choice=="quit"):
		print s.recv(100)
		s.close()
		break
