import socket
import sys

try:
	#create an AF_INET (IPv4), STREAM socket (TCP), returns a socket descriptor
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#except socket.error, msg:
except socket.error:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error Message: ' + str(msg[1])
	#print 'Failed to create socket'
	sys.exit()

print 'Socket Created'


host = 'www.google.com'
port = 80

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

print 'IP address of ' +  host + ' is ' + remote_ip

s.connect((remote_ip, port))

print 'Socket connected to ' +  host + ' on ip ' + remote_ip


# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
	s.sendall(message)
except socket.error:
	print "Socket Failed"
	sys.exit()

print "Message sent successfully"

# Receive reply
reply = s.recv(4096)

print reply



