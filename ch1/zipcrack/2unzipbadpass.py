import zipfile
zFile = zipfile.ZipFile("evil.zip")
try:
	zFile.extractall(pwd="noturpass")
except Exception, e:
	print e