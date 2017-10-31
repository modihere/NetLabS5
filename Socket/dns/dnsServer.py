import sys
import socket
import threading

dict1={}		#data structure used for storing name of the functional server and their details

class myThread1(threading.Thread):

	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter

	def run(self):
		register()

def register():
	global dict1,host,port1,s2
	con2,adr2=s2.accept()
	while(1):
		l=con2.recv(1)
		ad=con2.recv(200)
		print "l=",l,"ad=",ad
		print "server for operation ",str(l)," is registered at ",con2," and ",adr2,"\n"
		dict1[l]=ad
		con2.close()
		con2,adr2=s2.accept()

class myThread2(threading.Thread):
	
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter

	def run(self):
		sendDetails(self.threadID)

def sendDetails(con):
	global dict1
	con.send("Enter the symbol of the calculation you want to perform(i.e '+' for add)\nEnter q for quit\n")
	while(1):
		req=con.recv(20)
		if(str(req)=="q"):
			break
		elif req in dict1:
			con.send(dict1[req])
			break
		else:
			con.send("error")	#no such calculation exist
	con.close()
		

host="localhost"
port=7008		#for listening clients request
port1=7009		#for listening request from different types of function server for registering them
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)	#socket for handling client request
s1.bind((host,port))
s1.listen(10)

s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)	#socket for registering function server
s2.bind((host,port1))
s2.listen(10)

print "DNS SERVER HAS STARTED\n"

thread1=myThread1(1,"Thread1",2)			#this thread is for registering the function server
thread1.start()

while(1):
	i=0
	con,adr=s1.accept()
	print "connection established by",con," , ", adr
	i=i+1
	name="Thread"+str(i)
	thread2=myThread2(con,name,i)
	thread2.start()
