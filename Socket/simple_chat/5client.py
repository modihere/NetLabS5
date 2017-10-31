#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

name=raw_input("Enter your name: ")
name="@"+name+">"
print "now you can start your chat.."
while 1:
	print name+">>"
	string= raw_input()
	msg= name+","+string
	
	s.send(msg)

	data = s.recv(50)
	print data
	

        if data=="quit": break
	if string=="quit": break

        
s.close()
