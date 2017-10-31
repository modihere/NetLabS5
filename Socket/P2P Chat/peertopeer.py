#!usr/bin/env python
import socket
import os
import sys
import threading

def main():

	class chatServer(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
			self.host = 'localhost'
			self.port = 5006
			self.flag = True
			self.exception = None
		def run(self):
			HOST = self.host
			PORT = self.port
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			try:
				s.bind((HOST,PORT))
			except Exception, e:
				chatclient.start()
				return
			finally:
				s.listen(1)
				self.conn, self.addr = s.accept()
				while self.flag == True:
					data = self.conn.recv(1024)
					if data:
						print "\nPeer>" + data
		def kill(self):
			self.flag = False
		def getException(self):
			return self.exception

	class chatClient(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
			self.host = 'localhost'
			self.port = 5006
			self.flag = True
		def run(self):
			HOST = self.host
			PORT = self.port
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((HOST,PORT))
			while self.flag == True:
				data = self.sock.recv(1024)
				if data:
					print "\nPeer>" + data
		def kill(self):
			self.flag = False

	class inputText(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
			self.flag = True
		def run(self):
			while self.flag == True:
				print 'You>',
				data = raw_input()
				try:
					chatclient.sock.sendall(data)
				except:
					Exception
				try:
					chatserver.conn.sendall(data)
				except:
					Exception
		def kill(self):
			self.flag = False

	chatclient = chatClient()
	chatserver = chatServer()
	chatserver.start()
	inputtext = inputText()
	inputtext.start()

if __name__ == "__main__":
	main()
