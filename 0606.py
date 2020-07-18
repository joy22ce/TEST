import tkinter as tk
import tkinter.messagebox as tkMessageBox
from PIL import Image, ImageTk
from tkinter import ttk


top = tk.Tk()

#介面
top.title('Test')
top.geometry("800x900+300+100")
top.configure(bg='#F2E6E6')


#卷軸
scrollbar = tk.Scrollbar(top)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


#標題
header_label = tk.Label(top, text='單元名稱:', bg='#F2E6E6', font='jf-openhuninn-1.1')
header_label.place(x=10, y=5)

#
# canvas = tk.Canvas(top, width=650, height=250, scrollregion=(0, 0, 520, 520))
# canvas.place(x=0, y=35)
# frame = tk.Frame(canvas)
# frame.place(width=630, height=250)
# vbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
# vbar.place(x=0, width=20, height=250)
# vbar.configure(command=canvas.yview)
# canvas.config(yscrollcommand=vbar.set)
# canvas.create_window((90, 240), window=frame)


# 圖片
def resize(w, h, w_box, h_box, im):
	f1 = 1.0*w_box/w
	f2 = 1.0*h_box/h
	factor = min([f1, f2])
	width = int(w*factor)
	height = int(h*factor)
	return im.resize((width, height), Image.ANTIALIAS)


w_box = 400
h_box = 400
im = Image.open("yahoo.jpg")
w, h = im.size
im_resized = resize(w, h, w_box, h_box, im)
tk_Image1 = ImageTk.PhotoImage(im_resized)
imLabel = tk.Label(top, image=tk_Image1)
imLabel.pack()

img = Image.open("aaa.jpg")
w2, h2 = img.size
img_resized = resize(w2, h2, w_box, h_box, img)
tk_Image2 = ImageTk.PhotoImage(img_resized)
imgLabel = tk.Label(top, image=tk_Image2)
imgLabel.pack()

img = Image.open("aaa.jpg")
w2, h2 = img.size
img_resized = resize(w2, h2, w_box, h_box, img)
tk_Image3 = ImageTk.PhotoImage(img_resized)
imgLabel = tk.Label(top, image=tk_Image3)
imgLabel.pack()


#文字標籤
label1 = tk.Label(top, text='哇哈哈', bg='skyblue', fg='blue', font='jf-openhuninn-1.1')
label1.place(x=0, y=50)
label1.pack()
label2 = tk.Label(top, text='2')
label2.place(x=33, y=33)
label2.pack()


#按鍵 視窗
def Hello():
	tkMessageBox.showinfo('Hello', 'Hellooooo')
	tkMessageBox.showinfo('HeHe', 'HAHAHA')


#按鈕
Handin = tk.Button(top, text=' Hand in ', command='Hello', font='jf-openhuninn-1.1')
Handin.pack(side=tk.BOTTOM)


top.mainloop()








