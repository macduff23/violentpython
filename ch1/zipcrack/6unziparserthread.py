#import your modules, optparse is new, used to parse command line arguments.

import zipfile
import optparse
from threading import Thread

#this is similar to what we've done before...
def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print '[+] Found password ' + password + '\n'
	except:
		pass

#let's get weird i guess.
#defining the parser responses and inputs
def main():
#first we print help text. 
	parser = optparse.OptionParser("usage%prog "+ "-f <zipfile> -d <dictionary>")
#now we add two options, zipname and dictionaryname as strings. 
	parser.add_option('-f', dest='zname', type='string', help='specify zip file')
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
#parser parses them
	(options, args) = parser.parse_args()
#print the help instructions if something doesn't get an argument.
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
#if you have arguments, populate these variables. 
	else:
		zname = options.zname
		dname = options.dname
#now we do what we've been doing on the new variables. 
	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()
#do it.
if __name__ == '__main__':
	main()	
	