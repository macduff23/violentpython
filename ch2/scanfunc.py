#import your modules
import optparse
from socket import *

#define the first function to scan the host and port
def connScan(tgtHost, tgtPort):
#
#try to connect to the socket, print that it's open, and close the connection
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		print '[+]%d/tcp open'% tgtPort
		connSkt.close
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
