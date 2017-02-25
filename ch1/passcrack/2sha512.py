import crypt
#this was not necessary!
import hashlib

def testPass(cryptPass):
#This is where the real action was at. I was such a fool!!!!
#This article made it simple for me: http://security.stackexchange.com/questions/108872/unable-to-get-correct-base-for-cracking-crypt3-sha-512-on-linux-with-python
#The gist of it is python crypt library will interpret sha512 hashes correctly ONLY IF YOU TELL IT TO 
#By swapping out the hashed passwords for sha-512 hashes and changing how cryptPass is parsed
#We pull in the salt but also include the $6$ which tips of crypt to hash it correctly. 
        salt = cryptPass[0:11]
        dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
                if (cryptWord == cryptPass):
			print "[+] Found PAssword: "+word+"\n"
			return
	print "[-] Password not found.\n"
	
        print "[debug] salt = "+salt+"\n"
#        print "[debug] cryptWord = "+cryptWord
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
