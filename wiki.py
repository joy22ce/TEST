import urllib.request as req
import bs4
import re

url = 'https://zh.wikipedia.org/wiki/NU%27EST'

with req.urlopen(url) as response:
	data = response.read().decode('utf-8')

root = bs4.BeautifulSoup(data, 'html.parser')

titles = root.find_all('span class')

for i in titles:
	print(i.string)





