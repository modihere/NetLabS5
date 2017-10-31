import sys
import socket
import threading

class myThread1 (threading.Thread):
	global s,con
	def __init__(self, threadID, name, counter):
        	threading.Thread.__init__(self)
        	self.threadID = threadID
       		self.name = name
        	self.counter = counter
	def run(self):
        	msgRecv(s,con)

class myThread2 (threading.Thread):
	global s,con
	def __init__(self, threadID, name, counter):
        	threading.Thread.__init__(self)
        	self.threadID = threadID
       		self.name = name
        	self.counter = counter
	def run(self):
        	msgSend(s,con)

def msgRecv(s,con):
	while(1):
		data = con.recv(50)
		print "\t\t"+data
		if(data=="quit"):
			con.close()
			exit(1)

def msgSend(s,con):

	global name
	while(1):
		print " "+name+">>"
		string= raw_input()
		msg= name+","+string
	
		con.send(msg)

		if(string=="quit"):
			con.close()
			exit(1)

host='localhost'
port=6006

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
name=raw_input("Enter your name :")
name='@'+name+'>'
print name," waiting ....."

con,ad=s.accept()

# Create new threads
thread1 = myThread1(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

