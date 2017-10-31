import socket
import sys
import threading

class myThread1(threading.Thread):
	global s,con
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	def run(self):
		msgSend(s,con)
		
def msgSend(s,con):
	while(1):
		con.send('Enter the operation(download or upload or quit):\n')
		choice=con.recv(100)
		if(choice=="download"):
			f1=open("avail_Files",'r+')
			con.send("choose name of file from the following list of files:\n\n")
			l=f1.read(100)
			while(len(l)!=0):
				con.send(l)
				l=f1.read(100)
				#if(len(l)==0):
				#	con.send("exit")
				#	break
				#con.send(l)
			f1.close()
			con.send("exit")
			print "list of files sent successfully\n"		########################################

			data=con.recv(100)

			f2=open(data,'rb+')
			print "file ",data, "is opened"
			while(1):
				line=f2.read(1024)
				if(len(line)==0):
					break
				con.send(line)
			f2.close()
			#con.send("quitt")
			print "file sent successfully\n"
			con.send("file sent successfully\n")

		elif(choice=="upload"):
			f1=open("avail_Files",'a+')
			con.send("enter the name of the file you want to upload")
			filename=con.recv(100)
			filename="uploaded_"+str(filename)
			f2=open(str(filename),'wb')
			#con.send(" ")				#this is a notification to the client that he can start uploading now
			data=con.recv(1024)
			while(len(data)!=0):
				f2.write(data)
				data=con.recv(1024)
			f2.close()
			f1.write(filename)
			f1.close()
			print con.recv(1024)
		
		elif(choice=="quit"):
			con.send("bye")
			con.close()
			break
				
							

host="localhost"
port=5003
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
print s

print "Server is waiting for request"
print 'you can upload/download a file.'
print "please be carefull writting filename, it is case sensetive.."
print"==============================================================="

while(1):
	i=0
	con,adr=s.accept()
	print "connection established by",con," , ", adr
	i=i+1
	name="Thread"+str(i)
	thread1=myThread1(i,name,i)
	thread1.start()
	


