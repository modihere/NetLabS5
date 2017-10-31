import sys
import socket
import threading

class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	def run(self):
		handleClient(self.threadID)

def handleClient(con):
	con.send("Enter two operands for substraction")
	op1=con.recv(100)
	op2=con.recv(100)
	print "for substraction given inputs are :",int(op1)," ",int(op2)
	result=int(op1)-int(op2)
	con.send(str(result))
	con.close()

host="localhost"
DnsPort=7009

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((host,DnsPort))
s1.send('-')
s1.send(str(8002))
s1.close()

AddServPort=8002
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((host,AddServPort))
s1.listen(10)
i=0

while(1):
	i=i+1	
	name="Thread"+str(i)
	con,adr=s1.accept()
	print "request from client ",con," ",adr
	thread=myThread(con,name,i)
	thread.start()
