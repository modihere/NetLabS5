import sys
import threading
import socket


class myThread1 (threading.Thread):
	global s
	def __init__(self, threadID, name, counter):
        	threading.Thread.__init__(self)
        	self.threadID = threadID
        	self.name = name
        	self.counter = counter
	def run(self):
        	msgRecv(s)

class myThread2 (threading.Thread):
	global s
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
	        self.name = name
	        self.counter = counter
	def run(self):
	        msgSend(s)

def msgRecv(s):
	
	while(1):
		data=s.recv(50)
		print "\t\t",data
		if(data=="quit"):
			s.close()
			exit(1)

def msgSend(s):

	global name
	while(1):
		print " "+name+">>"
		string= raw_input()
		msg= name+","+string
	
		s.send(msg)

		if(string=="quit"):
			s.close()
			exit(1)


host="localhost"
port=6006

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

name=raw_input("Enter your name: ")
name="@"+name+">"
print "now you can start your chat.."

# Create new threads
thread1 = myThread1(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

		
