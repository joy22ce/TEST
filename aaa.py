import tkinter as tk
import tkinter.messagebox as tkMessageBox
from PIL import Image, ImageTk

top = tk.Tk()

top.title('Test')
top.geometry('1000x1000')
top.configure(bg='#F2E6E6')



canvas = tk.Canvas(top, width=200, height=180, scrollregion=(0, 0, 520, 520))
canvas.place(x=75, y=265)
frame = tk.Frame(canvas)
frame.place(width=180, height=180)
vbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
vbar.place(x=180, width=20, height=180)
vbar.configure(command=canvas.yview)
hbar = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
hbar.place(x=0, y=165, width=180, height=20)
hbar.configure(command=canvas.xview)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.create_window((90, 240), window=frame)


top.mainloop()
