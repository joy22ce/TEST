### Class 屬性
# class Room:
# 	supportedElem = ['bed', 'fan']
# 	def check(elem):
# 		if elem not in Room.supportedElem:
# 			print(elem, 'not supported')
# 		else:
# 			print('yes', elem, 'is in the room')
# Room.check('bed')

# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def show(self):
# 		print(self.x, self.y)
#
# 	def dist(self, TargetX, TargetY):
# 		a = ((TargetX-self.x)**2 + (TargetY-self.y)**2)**0.5
# 		return a
#
# P1 = Point(1, 5)
#
# ans1 = P1.dist(1, 1)
# print(ans1)
# ans2 = P1.dist(0, 0)
# print(ans2)


# f = open('text.txt', 'r')
# print(f.read())
# f.close()

# class File:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def open(self):
# 		self.file = open(self.name, 'r')
#
# 	def print(self):
# 		print(self.file.read())
#
# 	def close(self):
# 		self.file.close()
#
# f = File('text.txt')
# f.open()
# f.print()
# f.close()
#
# f2 = File('text2.txt')
# f2.open()
# f2.print()
# f2.close()


### 撲克牌隨機分配四人
# import random
#
# A = ''
# B = []
# for i in ['!', '@', '#', '$']:
# 	for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
# 		A = A + i + j
# 		B.append(A)
# 		A = ''
# print(random.sample(B, 13))


# class calculator:
#
# 	def __init__(self, name, price):
# 		self.n = name
# 		self.p = price
#
# 	def add(self, a, b):
# 		print(a + b)
#
# 	def minus(self, a, b):
# 		print(a - b)
#
# 	def time(self, a, b):
# 		print(a * b)
#
# 	def divi(self, a, b):
# 		print(a / b)
#
# cA = calculator('A', 154)
# cA = calculator.add(5, 3)

# import time
# print('aaa')
# time.sleep(5)














