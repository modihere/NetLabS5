#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print "select a number for operation :"
print "1.Add"
print "2.sub"
print "3.mul"
print "4.div"
print "please input: "
select=input()

x=input("enter x: ")
y=input("enter y: ")
string=""
if select==1: 
	string= "add"+","+str(x)+","+str(y)
elif select==2: 
	string= "sub"+","+str(x)+","+str(y)
elif select==3: 
	string= "mul"+","+str(x)+","+str(y)
if select==4: 
	string= "div"+","+str(x)+","+str(y)
print select, string
s.send(string)
data = s.recv(50)

s.close()

print 'Received'
print "========calculation of 2 int number=========="
print "opration(x,y)= :",int(data)

