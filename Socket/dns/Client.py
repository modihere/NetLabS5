import sys
import socket
import ast

host="localhost"
port=7008
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((host,port))

msg=s1.recv(200)
while(1):
	print msg			#this portion communicate with dns server
	op=raw_input()
	s1.send(op)
	if(op=="q"):
		break
	msg1=s1.recv(300)
	if(str(msg1)=="error"):
		print "NO SUCH OPERATION EXISTS"
		continue

	else:			#this portion communicate with the actual server				
		host2="localhost"
		ADR=int(msg1)
		s2.connect((host2,ADR))
		print s2.recv(100)
		op1=int(input("operand 1 : "))
		s2.send(str(op1))
		op2=int(input("operand 2 : "))
		s2.send(str(op2))
		print op1," ",op," ",op2," = ",s2.recv(1024)

s2.close()
s1.close()
