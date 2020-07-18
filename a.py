
# a = 3
# print(a)
# b = 'hello world'
# c = b.replace('world','python')
# print(c)
# d = '*'
# print('  '+d+'  '+'\n'+' '+d+' '+d+' '+'\n'+d+' '+d+' '+d)

### str to int
# input('good morning birthday') #
# A = input('請問你的出生年分？')
# B = input('請問今年幾年?')
## A = int(A)
## B = int(B)
# age = (B-A)
##
# print(age)
# C = input('小朋友個數?')
# D = input('糖果個數?')
# C = int(C)
# D = int(D)
# candy = (C//D,C%D)
# print(candy)

###list append '+=' /tuple不可變更 cf. list
# AAA_list = ['aaa','bbb','ccc']
# AAA_list.append('ddd')
# print(AAA_list)
# AAA_list += ['eee'] # += ()內的每個字會用逗號隔開
# print(AAA_list)

### .insert .remove
# AAA_list = ['aaa','bbb','ccc']
# AAA_list.insert(2,100)
# print(AAA_list)
# del AAA_list[3]
# print(AAA_list)
# AAA_list.remove(100)
# print(AAA_list)

# ZZZ_list = ['aaa','ccc','aaa','bbb']
# ZZZ_list.remove('aaa')
# print(ZZZ_list)

### sorted 暫時/sort 永久
# sort_list = ['aaa','ccc','fff','aa']
# sor = sorted(sort_list)
# print(sor)
# sort_list.sort()
# print(sort_list)

##多重list
# list_A = [[1,2,3],[4,5,6,7]]
# print(list_A[1][:-1])

### pop 將資料從最後一個開始取出(不放回)
# list_S = [1,2,3,4,5,6,7]
# a = list_S.pop() #取出7
# print(a) # a=7
# print(list_S) # list_S = [1~6]
# b = list_S.pop() #取出6
# print(b) # b = 6
# print(list_S) #list_S = [1~5]

### 作業
# A = input('請輸入16碼數字')
# len = len(A) #數值
# len2 = 16-len #要補幾個0
# print(len2*'0'+A)

### if 自行練習
# A = input('輸入數字')
# B = 4
# A = int(A)
# if A-B < 0 :
#      print('wrong')
# elif A-B == 0 :
#      print('same')
# else :
#      print('right')

### if 作業練習
# A = input('plz enter 16 numbers')
# len = len(A)
# if len > 16:
#     print(A[0:16])
# elif len == 16:
#     print(A)
# else:
#     while len < 16:
#         A = ('0'+A)
#         len = len+1
#     print(A)

# A = input('plz enter a number')
# num = int(A)
# if num > 200:
#     print('it is over 200')
# elif 100 < num < 200:
#     print('it is between 100 and 200')
# elif num == 100:
#     print('100')
# elif num == 200:
#     print('200')
# else:
#     print('it is less than 100')

### dic 用法
# dic_A = {'A':'ant','B':'bird','C':'cat','c':'candy'}
# print(dic_A.keys())
# print(list(dic_A.values()))
# print(list(dic_A.items()))
# dic_A['D'] = 'dog'
# print(dic_A)

### for迴圈 用法
#
# list_A = [0,1,2,3,45]
# B = 0
# for i in list_A:
#     print(i)
#     B = B + 1
# print(B)

### range 用法
# print('plz enter 2 numbers')
# A = int(input('first'))
# B = int(input('second'))
# for z in range(A,B):
#     if z**2 < B:
#         print(z**2)
#     else:
#         break


### while 用法
# print('輸入q則結束')
# while True:
#     B = input('判斷偶數')
#     if B == 'q':
#         break
#     elif int(B)%2 == 1:
#         print('基數')
#     elif int(B)%2 == 0:
#         print('偶數')
#     else:
#         print('都不是')

###兩個以上的input
# a,b = input('plz enter 2 numbers:(a,b)').split(',')
# print(a,b)

###金字塔作業
# i = a = int(input('金字塔層數'))
# b = a-1                         #空白數
# c = 0
# for i in range(1,(i+1)):
#     print(b*' '+'*'+c*' *')
#     b -= 1
#     c += 1

#     *4
#    * *3
#   * * *2
#  * * * *1
# * * * * *0

# a_list = [1000, 5, 4, 1, 2]
# # result_list = []
# # # a = input(' ')
# # # number = len(a_list)
# # min = 100
# # for i in range(0, len(a_list)):
# # 	# print('-----------------------')
# # 	# print("a: ", a_list[i], ", min: ", min)
# # 	if a_list[i] < min:
# # 		min = a_list[i]
# # 		# print('change! ', min)

# print(min)

###
# min_index = 0
# for i in range(0, len(a_list)):
# 	if a_list[i] == min:
# 		min_index = i

# print(min_index)
# result_list.append(a_list[min_index])
# del a_list[min_index]
# print('a_list: ', a_list)
# print('result_list: ', result_list)

# a = [3,5,4,1,2]

# for
# 	if a[0] > a[1]:
# 		a[0] = tmp
# 		a[0] = a[1]
# 		a[1] = tmp
# print(a)

# a_list = [1000, 5, 4, 1, 2]
# result_list = []
#
# for i in range(0, len(a_list)):
# 	min = 100    #設 要替換的最小值變數
# 	min_index = 0#設 此變數的位置
# 	#print('i: ', i)
# 	for j in range(0, len(a_list)):
# 		#print('j: ', j)
# 		if a_list[j] < min:#將最小值替換為變數
# 			min = a_list[j]#將最小值替換為變數
# 	for k in range(0, len(a_list)):
# 		#print('k: ', k)
# 		#print('a_list: ', a_list)
# 		if a_list[k] == min:#找出最小值變數在哪個位置
# 			min_index = k #此位置變數
# 	result_list.append(a_list[min_index]) #將找出的最小值放入替換list
# 	del a_list[min_index] #將原list最小值刪除
#
# print('result_list: ', result_list)

# a = 0
# for i in range(1, 11):
# 	a = a+i
# print(a)

# for i in range(1, 10):
# 	for j in range(1, 10):
# 		print(i*j)



from PIL import Image, ImageTk
import tkinter as tk

top = tk.Tk()

def resize(w, h, w_box, h_box, im):
	f1 = 1.0*w_box/w
	f2 = 1.0*h_box/h
	factor = min([f1, f2])
	width = int(w*factor)
	height = int(h*factor)
	return im.resize((width, height), Image.ANTIALIAS)

scrollbar = tk.Scrollbar(top)
scrollbar.pack(side="right", fill="y")

w_box = 400
h_box = 400

im = Image.open("yahoo.jpg")
w, h = im.size
im_resized = resize(w, h, w_box, h_box, im)
tk_Image = ImageTk.PhotoImage(im_resized)
imLabel = tk.Label(top, image=tk_Image)


listbox = tk.Listbox(top, yscrollcommand=scrollbar.set)
listbox.insert('end', im)
listbox.insert("end", 'aaa')
listbox.pack(side="left", fill="both")
imLabel.pack()
scrollbar.config(command=listbox.yview)

top.mainloop()









