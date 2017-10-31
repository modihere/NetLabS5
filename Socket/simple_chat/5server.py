#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(20)
print "I am online.."

name=raw_input("Enter your name:")
name="@"+name+">"
print "waiting..."
conn, addr = s.accept()
 
while 1:
	data = conn.recv(50)
	print "\t\t"+data
	print " "+name+">>"
	string= raw_input()
	msg= name+","+string
	
	conn.send(msg)

	
    if data=="quit": break
	if string=="quit": break

        
conn.close()
