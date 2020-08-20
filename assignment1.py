import urllib.request
import re

response = urllib.request.urlopen("https://www.york.ac.uk/teaching/cws/wws/webpage1.html")
html = response.read().decode('utf-8')

clean = re.compile('<.*?>')
text = re.sub(clean, '',html)
#print(text.strip())

with open("scraping-text.txt", 'w') as f:
    f.write(text.strip())
