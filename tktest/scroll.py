#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps

root = tk.Tk()
root.geometry("400x800")

canvas = tk.Canvas(root, bg='cyan')
canvas.place(x=0,y=0,width=400,height=800)

bar = tk.Scrollbar(root, orient=tk.VERTICAL)
bar.pack(side=tk.RIGHT, fill=tk.Y)

bar.config(command=canvas.yview)

canvas.config(scrollregion=(0,0,0,1200))

canvas.config(yscrollcommand=bar.set)

frame = tk.Frame(canvas)

canvas.create_window((0,100), window=frame, anchor=tk.NW, width=canvas.cget('width'))

fig1 = Image.open("fig1.png")
fig1 = fig1.resize(size=(200,200))
img = ImageTk.PhotoImage(fig1)

imglabel = tk.Label(frame, image=img)
imglabel.grid(column=0, row=0)
button = tk.Button(frame, text="hoge")
button.grid(column=1, row=0)

def button_clicked(event):
	print(event)
	imglabel1 = tk.Label(frame, image=img)
	imglabel1.grid(column=0, row=1)

button.bind("<ButtonPress>", button_clicked)

root.mainloop()
