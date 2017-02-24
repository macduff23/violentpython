#This script doesnt work, but is just a sample of what I did along the way to figure out what my problem was

import crypt
import hashlib

def testPass(cryptPass):
        salt = cryptPass[0:11]
        dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = hashlib.sha512(word + salt)
                if (cryptWord == cryptPass.split('$')[3].split(':')[0]):
			print "[+] Found PAssword: "+word+"\n"
			return
	print "[-] Password not found.\n"
	
#This was very useful for me to figure out what I needed to do.
#While this script didnt work, using the print function to print what your variables are lets you know what your script is doing
#smart stuff. 

        print "[debug] salt = "+salt+"\n"
        print "[debug] cryptPass = "+cryptPass
        return

def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
                    user = line.split(':')[0]
                    cryptPass = line.split(':')[1].strip(' ')
                    print "[*] Cracking Password For: "+user
                    testPass(cryptPass)
if __name__ == "__main__":
        main()
