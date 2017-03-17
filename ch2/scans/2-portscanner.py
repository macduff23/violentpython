#import your modules cause you need them
import optparse
import socket
from socket import *

#define the first function to scan the host and port

def connScan(tgtHost, tgtPort):

##try to connect to the socket, print that it's open, and close the connection
##We added the send ViolentPython and results bit

	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)
		print '[+]%d/tcp open'% tgtPort
		print '[+] ' + str(results)
		connSkt.close()

#throw and error if it doesn't work

	except:
		print '[-]%d/tcp closed'% tgtPort

#now we port scan it. See if you can connect o it and if you can't throw an error.
#This is the portScan funciton that reuses the connScan one over and over to scann ports

def portScan(tgtHost, tgtPorts):

	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print"[-] Cannot resolve '%s': Unknown host"%tgtHost
		return

#also see if you can resolve the IP to a hostname

	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP

#set a timeout for 1 second and for loop the modules above.

	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print 'Scanning port ' + tgtPort
		connScan(tgtHost, int(tgtPort))


#this is the parser.py I cat'ed >> to the end of this file
#I also had to modify some stuff, like i changed line breaks to one line, and tgtPorts splits now

def main():

#parsing things and first we print the usage in case theres an error
#we added two options, -H and -p to pull hosts and ports. I had tochange int to string for Ports

	parser = optparse.OptionParser("usage%prog -H <target host> -p <target port>")
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')

#now we parse them and for loop through a port scan
#note the tgtPorts - if you don't split the string at comma space, you'll end up pulling each integer one by one instead of the full port number like 21

	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
#this is from the book but its wrong!
#see here: http://stackoverflow.com/questions/17807992/violent-python-port-inputs-not-being-seperated 
#	tgtPorts = str(options.tgtPort).split(', ')
#to run the command don't use spaces between ports. -H 1.1.1.1 -p 10,11,12,13
	tgtPorts = [p.strip() for p in options.tgtPort.split(',')]
	if (tgtHost == None) | (tgtPorts[0] == None):
		print '[-] You must specify a target host and port[s].'
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()
