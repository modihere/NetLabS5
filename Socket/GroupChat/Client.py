import sys
import socket
import threading

class myThread1(threading.Thread):
	
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter

	def run(self):
		msgSend()

def msgSend():
	global s,quit
	while(1):
		data=raw_input()
		s.send(data)
		if(data=="quit"):
			quit=1
			break

class myThread2(threading.Thread):
	
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter

	def run(self):
		msgRecv()

def msgRecv():
	global s,quit
	while(1):
		print "\n",s.recv(100)
		if(quit==1):
			break

host="localhost"
port=6001

quit=0		#This shows whether this client has quit the chat yet or not. quit=0 means not yet

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)										
s.connect((host,port))
print s.recv(100)
name=raw_input()
s.send(name)
print s.recv(150)
print "================================================================================================"

thread1=myThread1(1,"Thread1",2)
thread1.start()

thread2=myThread2(2,"Thread2",3)
thread2.start()
