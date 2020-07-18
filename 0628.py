### 爬資料

# import json
# import urllib.request as request
#
# src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
#
# with request.urlopen(src) as response:
# 	data = json.load(response)
#
# list(data)
# list = data["result"]["results"]
#
# path = '/Users/USER/Desktop/new_file.txt'
# data_A = open(path, 'w', encoding="utf-8")
#
# for company in list:
# 	print(company['公司名稱'], end='\t')
# 	print(company['公司地址'])
# 	a = company['公司名稱']+'\t'+company['公司地址']+'\n'
# 	data_A.write(str(a))
#
#
# print('write sth to the new file')
#
# # data_A.write(A)
#
# print('well done')
# data_A.close()


import json
import urllib.request as request

src = "https://data.taipei/api/v1/dataset/7bcd8da2-06a8-4f22-8ff0-324a1369c106?scope=resourceAquire"

with request.urlopen(src) as response:
	data = json.load(response)

list(data)
list = data['result']['results']

path = '/Users/USER/Desktop/new_file.txt'
data_A = open(path, 'w', encoding="utf-8")

for company in list:
	print(company['Bus'], end='\t')
	print(company['Destination'])
	a = company['Bus']+'\t'+company['Destination']+'\n'
	data_A.write(str(a))


print('write sth to the new file')

# data_A.write(A)

print('well done')
data_A.close()






















