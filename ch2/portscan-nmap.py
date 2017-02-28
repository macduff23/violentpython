#Windows 10, python 2.7 - all done in powershell - THIS DID NOT WORK AS IS
#First i pip install nmap as admin, didn't work
#Had to manually extract and install python - http://xael.org/pages/python-nmap-en.html
#take the "nmap" folder it creates and use that to overwite the one created by pip install. that'll do it.

#let's import the modules
import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	nmScan.scan(tgtHost, tgtPort)
	state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	print "[*] " + tgtHost + " tcp/"+tgtPort +" "+state
def main():
#
#first we parse the options - you can reuse this general pattern quite a bit i think...
#
	parser = optparse.OptionParser('usage%prog -H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by commas in \"\'s')
	(options, args) = parser.parse_args()
#these values should match your dest's in the add_options
	tgtHost = options.tgtHost
#This split only works if you enclose your port values in quotes - "21, 22, 23"
	tgtPorts = str(options.tgtPort).split(', ')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	for tgtPort in tgtPorts:
		nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
	main()	
	