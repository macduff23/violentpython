#let's get our module
import optparse

#parsing things and first we print the usage in case theres an error
parser = optparse.OptionParser('usage %prog -H'+\
'<target host> - <target port>')

#first option -H
parser.add_option('-H', dest ='tgtHost', type='string', \
help='specify target host')
#2nd option -p
parser.add_option('-p', dest='tgtPort', type='int', \
help='specify target port')
#now we parse them
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) | (tgtPort == None):
	print parser.usage
	exit(0)
