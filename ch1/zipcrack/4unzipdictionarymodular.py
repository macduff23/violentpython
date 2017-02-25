#first we import the module we need. 
import zipfile
#define extractfile
#the way this is written it is expecting a zipfile and a password
def extractFile(zFile, password):
#zFile has an extractall action called pwd taht will accept a password to unzip a file and here it goes.
	try
		zFile.extractall(pwd=password)
		return password
#it tries the password and if it fails it returns to try again
	except:
		return
#This is our main function that uses the module above. 
def main():
#pull in the target file
	zFile = zipfile.ZipFile('evil.zip')
#create passFile with multiple lines from the dictionary.txt file
	passFile = open('dictionary.txt')
#read each line 
	for line in passFile.readlines():
#strip new line characters, we only want the word
	password = line.strip('\n')
#attempt to extract file with password. if it works exit and print password.
		guess = extractFile(zFile, password)
		if guess:
			print '[+] Password = ' + password + '\n'
			exit(0)
#do it.
if __name__ == '__main__'
	main()