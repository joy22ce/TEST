### 函式 計算英文，數字，空白的個數
# def count(n1):
# 	eng = num = space = 0
# 	for i in range(len(n1)):
# 		if str.isalpha(n1[i]) is True:
# 			eng += 1
# 		elif str.isdigit(n1[i]):
# 			num += 1
# 		elif str.isspace(n1[i]):
# 			space += 1
# 	print('eng: ', eng, 'num: ', num, 'space:', space)
# A = input('string')
# count(A)

### 遞迴 N階層(N!)
# def fact(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n*fact(n-1)
# A = fact(5)
# print(A)

### 遞迴 費氏數列
# def fibo(n):
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1
# 	return fibo(n-1) + fibo(n-2)
# print(fibo(10))

### 匯入套件
# import function
# A = function.add(1, 2)
# print(A)
#
# B = function.minus(3, 4)
# print(B)








