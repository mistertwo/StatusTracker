import urllib.request as urlreq
import sys

if len(sys.argv) < 2:
	print("need an article string to look for!")	
	sys.exit()

article_string = sys.argv[1]

open_index = 0
close_index = 0

user_agent = "Mozilla/5.0"
headers = {'User-Agent': user_agent}

webpage = urlreq.Request("http://danielturton.net", None, headers)
response = urlreq.urlopen(webpage)

parsed = str(response.read(), 'utf-8').split("\n")

for line in parsed:
	if article_string in line:
		open_index = parsed.index(line)
	if parsed[open_index].split(" ")[0] in line and parsed.index(line) > open_index:
		close_index = parsed.index(line)

print(parsed[open_index:close_index])
