import urllib2
try:
	urllib2.urlopen("http://google.com", timeout=3)
	print "YAY!!!! Connected to the internet"
except urllib2.URLError:
	print "Oops!!Check your connection"
