#misc test
Occassionally I'll create additional scripts to test my knowledge and make sure i can apply what i learned in the last chapter to this one. 
test.py in /misc test/ is an example of that, I'm trying to simply resolve a set of domains to IPs. 
I do this a lot with bash. In it's most basic form, it's something like this

```
for i in `cat sites`; do host $i >> results; done
```

i want to do this in python from now on because might as well. 