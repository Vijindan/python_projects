import urllib.request

with urllib.request.urlopen('http://google.ca/') as response:
	html = response.read()
	print(html)