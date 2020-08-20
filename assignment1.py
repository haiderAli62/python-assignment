import urllib.request

response = urllib.request.urlopen("https://www.york.ac.uk/teaching/cws/wws/webpage1.html")
html = response.read().decode('utf-8')


with open("scrapint-text", 'a') as f:
    f.write(html)
