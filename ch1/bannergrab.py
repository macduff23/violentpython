#first we import the socket module. This makes the toolset available to the script.

import socket

#Now we use the module.function() syntax. 
#Here, we use the socket modules setdefaulttimeout functionality to set a timeout to 2 seconds
# if it doesnt work in 2 seconds, we abort.

socket.setdefaulttimeout(2)

#Now we alias socket.socket() to s.
# Docs say "Create a new socket using the given address family, socket type and protocol number. The address family should be AF_INET (the default), AF_INET6 or AF_UNIX. The socket type should be SOCK_STREAM (the default), SOCK_DGRAM or perhaps one of the other SOCK_ constants. The protocol number is usually zero and may be omitted in that case."


s = socket.socket()

#Now we put in a conditional test. Try this, if it doesnt work, throw an exception
#using s we defined earlier, use the connect function to connect to this ip on this port

try:
    s.connect(("192.168.1.20",80))
    banner = s.recv(1024)
    return banner
except Exception, e:
    print "[-] Error = "+str(e)
