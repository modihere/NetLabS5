import sys
import socket
import threading
import os

os.system("rm history.txt")

clients=list()

class myThread(threading.Thread):
	
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter

	def run(self):
		handleClient(self.threadID)

def handleClient(con):
	global clients
	f1=open("history.txt",'a+')
	con.send("Enter your name : ")
	name=con.recv(100)
	name="@"+name+">>"
	con.send("Now you can Start your Chat (To quit enter quit || To request for history enter history)")
	while(1):
		data=con.recv(100)
		data1=name+data
		for i in range(len(clients)):
			clients[i].send(data1)
		f1.write(data1)
		f1.write("\n")

		if(data=="quit"):
			break

		elif(data=="history"):
			f1.close()
			f1=open("history.txt",'r')
			data=f1.read(100)
			while(len(data)!=0):
				con.send(data)
				data=f1.read(100)
			f1.close()
			f1=open("history.txt",'a+')

			
host="localhost"
port=6001

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
print "\nSERVER HAS STARTED"

i=0

while(1):
	con,adr=s.accept()
	print "connection established by client ",adr
	clients.append(con)
	i=i+1
	name="Thread"+str(i)
	thread=myThread(con,name,i)
	thread.start()
