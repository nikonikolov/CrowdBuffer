import socket
import sys
from thread import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error Message: ' + str(msg[1])
	#print 'Failed to create socket'
	sys.exit()
print 'Socket Created'
# End Socket Creation


# Bind Socket to a particular address and port
try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print "Bind failed. Error code: " + str(msg[0]) + " Error Message: " + str(msg[1])
	sys.exit()
print 'Socket Bind Complete'
# End Binding

# Make Socket Listen 
s.listen(100)
print "Socket Listening"

# Define a clientthread
def clientthread(conn):
	conn.send("welcome to server. type sth and hit enter\n")

	while True:
		data = conn.recv(1024)
		reply = "OK" + data
		# If data is not None
		if not data:
			break

		conn.sendall(reply)

	# Loop terminated, close connection
	conn.close()
# End clientthread

# Keep talking with Client
while 1:

	# Wait to accept a connection
	conn, addr = s.accept()

	#Display Client Information
	print "Connected with " + addr[0] + ":" + str(addr[1])

	start_new_thread(clientthread, (conn,))

# End talking with Client Loop	
s.close()




