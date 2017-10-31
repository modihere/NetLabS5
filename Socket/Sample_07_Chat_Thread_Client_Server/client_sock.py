#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    #command = raw_input('Bikash::::')
    #a = raw_input('Enter the First No.')
    #b = raw_input('Enter the Second No.')
    #c = raw_input()
    #command = command + '#'+ 'Bikash'
    #print command
    #if c=='\n':
     #  break
    s.send('client')
    reply = s.recv(1024)
    #if reply=='Quit':
    print reply
