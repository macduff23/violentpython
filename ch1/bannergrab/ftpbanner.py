import socket
def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return
def main()
	ip1 = '192.168.1.20'
	ip2 = '192.168.1.21'
	port = 80
:w
