#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import time

window = tk.Tk()
window.geometry("600x200")
window.title("hoge")

canvas = tk.Canvas(window)
canvas.pack(side=tk.LEFT, fill=tk.BOTH)
# canvas.place(width=400, height=800, x=0,y=0)

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar.config(command=canvas.yview)
canvas.config(scrollregion=(0, 0, 800, 0))
canvas.config(yscrollcommand=scrollbar.set)

frame = ttk.Frame(canvas)
frame.place(width=400, height=400,x=0,y=0)

fig1 = Image.open("fig1.png")
fig1 = fig1.resize(size=(200,200))
img = ImageTk.PhotoImage(fig1)

imglabel = ttk.Label(frame, image=img)
imglabel.place(x=0,y=0)
button = ttk.Button(frame, text="hoge")
button.place(x=200,y=0)

def button_clicked(event):
	imglabel.config(text="button pressed")
	# time.sleep(3)
	imglabel1 = ttk.Label(frame, image=img)
	imglabel1.place(x=0,y=200)

button.bind("<ButtonPress>", button_clicked)

window.mainloop()
