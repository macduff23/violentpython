This was a doozy. I don't know why it took me so long to figure out what is what. The easiest way to approach this is to:

###Use a dictionary that you know will work. 
I started with rockyou to crack stuff but it didnt have the simple egg password for the example. I added it. Eventually I just created a dictionary file with the passwords I knew would be in there. I don't need to wait 2 minutes for my VM to crunch thousands of passwords I know won't work. Use a known encrypted password and a known successful dictionary and your cracks will run faster and you'll have known values you're testing against. 

###This is simpler than you'd think.
Do some research about how python crypt encrypts and or hashes stuff. The article linked in my script set the light off in my head that I was doing it all wrong.

###Files

testpass.py - the original proof of concept script from the book. 

sha512.py - my debugging script. I printed variables after they were created so I could see what my script was doing. VERY HELPFUL

dictionary.txt - was rockyou copied from my kali wordlist directory, now its just a password file with the password I know it'll be

passwords.txt - i created a new user called taco and a password 123456. This was a good known value to test against.

2sha512.py - this one worked. Very few changes were made from the original script.
