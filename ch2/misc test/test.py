import socket

sites = open('sitestoresolve.txt','r')
for site in sites.readlines():
	siteURL = site.strip('\n')
	s = socket.gethostbyname(siteURL)
	print "[+] Site "+siteURL+" resolves to "+s