### 正規表示法 regular express
# import re
# #
# ptn = r'r[a-z]n'
# print(re.search(ptn, 'dogs run to eat'))
# #
# ptn = r'r[a-z0-9]n'
# print(re.search(ptn, 'dogs r1n to eat'))


# import re
# import bs4
# ptn = r's'
#
# string = '''
# hstfhbssssshkls
# '''
# a = re.findall(ptn, string)
# print(len(a))

import urllib.request as req
import bs4
import re

url = 'https://movies.yahoo.com.tw/movie_intheaters.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAALjcIx1Kd_9A38C_5G5dDJ7RAOlQk0vcTKO-DFG-gfLq75as6pnhrxQgk15aB33orHYUGPUubK81ritgXriWofUFqPNg8XB3LavrO8Gv3EwZAOol0EBjY8OtiG4HWs40ldAIrvzACoTYRdD0TIZs8WUoyhBFOc6WMLOljd_kxAeH'

with req.urlopen(url) as response:
	data = response.read().decode('utf-8')

root = bs4.BeautifulSoup(data, 'html.parser')

titles = root.find_all('option')

for i in titles:
	if 8 > len(i.get('value')) > 4:
		print(i.string)

#
# for i in titles:
# 	if i.get('data-name') != None:
# 		print(i.get('data-name'))
# 	else:
# 		print(end=' ')












































