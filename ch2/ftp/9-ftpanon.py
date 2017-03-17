#To make this work, I have a VM at the IP in 'host.' On that server i ran
#apt-get install pure-ftpd
#useradd ftp -d /home/ftp -m
#edited /etc/pure-ftpd/conf/noAnonymous to read "no"
#service pure-ftpd start

#import the necessary module
import ftplib

#define your function 

def anonLogin(hostname):

#hope it works. Login with anonymous and the email me@your.com and let me know
#if it worked.

    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print '\n[*] ' + str(hostname) + ' FTP Anonymous Login Succeeded'
        ftp.quit()
        return True
#if it didn't work, tell me and return False. The capital False (like True) is
#important
    except Exception, e:
        print '\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed'
        return False

#define your host and login.
host = '192.168.1.82'
anonLogin(host)
