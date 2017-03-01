#import your modules

import pxssh

# define sending commands.  we'll define command later. 
def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before

def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print '[-] Error connecting'
        exit(0)

s = connect('127.0.0.1', 'root','toor')
send_command(s, 'cat /etc/shadow | grep root')
