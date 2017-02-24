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
#We're doing this differently from the 2nd script
#We're going to iterate through a range of things instead of typing it all out


def main():

#first we define our port list and then we range our IPs
	portList = [21,22,25,80,110,443]
	for x in range(1, 25):

#we define ip as the ip plus the iterated string
#we then nest the port loop in the ip string we defined
#its easier if you cat this out to hid ethe comments 

		ip = '192.168.1.' + str(x)
		for port in portList:
			banner = retBanner(ip,port)
			if banner:
				print '[+] ' + ip + ': ' + banner
				checkVulns(banner)

	
#This is something I'm not sure I get. Main seems to do everything as its the main function. 
#Run it and all the other shit happens.
 
if __name__ == '__main__':
	main()
