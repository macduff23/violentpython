#import the socket module

import socket

#let's define the function retBanner, which will return the banner!
#We set the default timeout to 2 so it times out
#we define the s.connect so anytime we call retBanner, it connects to a port and socket
#then it recv's 1024 bytes back and prints it or returns and error which might be blank

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

#Let's check for vulnerabilities now
#We are defining checkVulns to look for text in the banner that matches stuff
#We could specify version numbers or other things if we wanted. 
#Note the use of if, elif, else.
#if x = true, then good if x = then else if else if else if until else

#it's important to get that banner is being treated as a variable and being checked against the checkVulns function.

def checkVulns(banner):
	if 'Tacos don\'t real' in banner:
		print '[+] ahh shit yum.'
	elif 'Pure-FTP' in banner:
		print '[+] PureFTP is vulnerable'
	elif 'ProFTP' in banner:
		print '[+] ProFTP is vulnerable'
	else:
		print '[-] FTP server is not vulnerable'
	return

#now we define the main function. This uses the functions we defined previously.
#we define a few IPs to connect to and specify the port that will be used.
#if its the first IP, it returns the IP and banner, same for the second.

def main():
	
#we tell it what IPs and ports to check
	ip1 = '192.168.1.1'
	ip2 = '192.168.1.20'
	ip3 = '192.168.1.10'
	port = 21

#This part tells it to take the results from the banner1 check and print whether or not its vulnerable

	banner1 = retBanner(ip1, port)
	if banner1:
		print '[+] ' + ip1 + ': \n ' + banner1
		checkVulns(banner1)
	else:
		print '[-] Service down at ' + ip1
#Again for 2

	banner2 = retBanner(ip2, port)
	if banner2:
		print '[+] ' + ip2 + ': ' + banner2.strip('\n')
		checkVulns(banner2)
	else:
		print '[-] Service at ' + ip2 + 'is down'

	banner3 = retBanner(ip3, port)
	if banner3:
		print '[+] ' + ip3 + ': ' + banner3
		checkVulns(banner3)
	else:
		print '[-] Service down at ' + ip3

#This is something I'm not sure I get. Main seems to do everything as its the main function. 
#Run it and all the other shit happens.
 
if __name__ == '__main__':
	main()
