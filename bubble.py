# a = 34
# tmp = a[0]
# a[0] = a[1]
# a[1] = tmp
# print(a)

# a_list = [1000, 5, 4, 1, 2]
# result_list = []
# for i in range(0, len(a_list)):
# 	min = 100
# 	min_index = 0
# 	for j in range(0, len(a_list)):
# 		if a_list[j] < min:
# 			min = a_list[j]
# 	for k in range(0, len(a_list)):
# 		if a_list[k] == min:
# 			min_index = k
# 	result_list.append(a_list[min_index])
# 	del a_list[min_index]
#
# print(a_list)
# print(result_list)
#設 要替換的最小值變數
#設 此變數的位置
#將最小值替換為變數
#將最小值替換為變數
#找出最小值變數在哪個位置
#此位置變數
#將找出的最小值放入替換list
#將原list最小值刪除



# a_list[1000, 5, 4, 1, 2]
# result_list[]
# for i in range(0, len(a_list)):
# 	min = 100
# 	min_index = 0
# 	for j in range(0, len(a_list)):
# 		if min > a_list[j]:
# 			min = a_list[j]
# 	for k in range(0, len(a_list)):
# 		if min == a_list[k]:
# 			min_index = k
# 	result_list.append(a_list[min_index])
# 	del a_list[min_index]
# print(result_list)

# a = 0
# for i in range(1, 10):
# 	a = a+i
# print(a)

### 棋盤
# for i in range(1, 11):
# 	if i % 2 == 0:
# 		for j in range(1, 6):
# 			print('██', end='  ')
# 	else:
# 		for k in range(1, 6):
# 			print('  ', end='██')
# 	print()

# 有一個整數小於 100,000，
# 他加上 100後是一個完全平方數，
# 再加上168又是一個完全平方數，
# 請問該數是多少？
# import math
# for i in range(100000):
# 	if math.sqrt(i + 100) == int(math.sqrt(i + 100)):
# 		if math.sqrt(i + 268) == int(math.sqrt(i + 268)):
# 			print(i)


# 有1、2、3、4個數字，
# 能組成多少個互不相同且無重複數字的三位數？
# 都是多少？
# count = 0
# for i in range(1, 5):
# 	for j in range(1, 5):
# 		for k in range(1, 5):
# 			if i != j & j != k & i != k:
# 				print(i,j,k)
# 				count += 1
# print(count)

# Q6 輸入某年某月某日，判斷這一天是這一年的第幾天？
# year, month, date = input('請輸入年月日 ex. 2020 04 11').split(' ')
# print(year, month, date)
# count = 0
# mon_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
#
# #判斷閏年
# if int(year) % 4 == 0:
# 	#閏年大於二月則加一天
# 	if int(month) > 2:
# 		count += 1
# 		# print('if: ', count)
#
# #加上已過的月份
# for i in range(0, int(month)-1):
# 	count += mon_list[i]
# 	print('count: ', count)
#
# #加上天數
# count += int(date)
#
# print(count)

### Q7 費式數列
# a_list = [1, 1]
# for i in range(20):
# 	A = a_list[i] + a_list[i+1]
# 	a_list.append(A)
# print(a_list)

### 找質數
# a_list = []
# for i in range(2, 100):
# 	a = 0
# 	for j in range(2, 100):
# 		if i % j == 0:
# 			a += 1
# 	if a == 1:
# 		a_list.append(i)
# print(a_list)

### bubble sort
# bubble_list = [1, 3, 5, 2, 4]
# # for j in range(13):
# # 	for i in range(0, 4):
# # 		if bubble_list[i] > bubble_list[i+1]:
# # 			A = bubble_list[i+1]
# # 			bubble_list[i+1] = bubble_list[i]
# # 			bubble_list[i] = A
# # print(bubble_list)

# A = 0
# for i in range(1, 11):
# 	A = A + i
# print(A)

### 函式 def function
# def sayHello():
# 	print('sayHello')
#
# sayHello()
# sayHello()
# sayHello()

# def say(msg):
# 	print(msg)
#
# say('Hello world')
# say('Hello python')
# say('Hello function')

### 函式 return/value
# def add(n1, n2):
# 	result = n1 + n2
# 	print(n1, '+', n2, '=', result)
# 	A = 'A'
# 	B = 'B'
# 	return A, B
#
# value1, value2 = add(5, 6)
# print(value1, value2)
# add(18, 20)


# def summary(n1):
# 	A = 0
# 	for i in range(1, n1+1):
# 		A = A + i
# 	print(A)
#
# summary(10)
# summary(20)
# summary(30)


### 建立/輸入文字進入.txt
# path = '/Users/USER/Desktop/0425.txt'
# open_file = open(path, 'r')
# read = open_file.read()
# print(read)

# new_path = '/Users/USER/Desktop/new_file.txt'
# new_days = open(new_path, 'w')
#
# print('write sth to the new file')
# title = 'write in new file!'
# new_days.write(title)
#
# print('well done')
#
# new_days.close()
# print('file close')

### import 時間
# import datetime
#
# today = datetime.datetime.now()
# print(today)

# import datetime
# new_path = '/Users/USER/Desktop/diary.txt'
# new_days = open(new_path, 'a+')


# title = 'My  Diary \n'
# new_days.write(title)
# time = datetime.datetime.now()
# new_days.write(str(time)+'\n')
#
# new_days.close()

### cmd 使電腦登出
# import os
# import time
# time.sleep(10)
# os.system('shutdown -l')





















