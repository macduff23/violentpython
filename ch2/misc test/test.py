import socket

sites = open('sitestoresolve.txt','r')
for site in sites.readlines():
	siteURL = site.strip('\n')
	s = socket.gethostbyname(siteURL)
<<<<<<< HEAD
	print "[+] Site "+siteURL+" resolves to "+s
=======
	print "[+] Site "+siteURL+" resolves to "+s
>>>>>>> 669ca63ea84c894a4684c0ae21b72f6bb6336e54
