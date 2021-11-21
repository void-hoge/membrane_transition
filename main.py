#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps

dbdir_path = "DBfigures/"
treefile_path = dbdir_path+"tree.txt"

class graph:
	data = []
	nodes = []
	path = []
	def __init__(self, path):
		all = open(path).read().split('\n')
		for line in all[:-1]:
			self.data.append(line.split())
		self.nodes = [edges[0] for edges in self.data]
		self.path.append(self.nodes[0])

	def next(self, current):
		if current not in self.nodes:
			return None
		idx = self.nodes.index(current)
		return self.data[idx][1:]

	def dump(self):
		print("data")
		for tmp in self.data:
			print(tmp)

class app:
	root = tk.Tk()
	canvas = tk.Canvas(root)
	bar = tk.Scrollbar(root, orient=tk.VERTICAL)
	frame = tk.Frame(canvas)
	img = {}
	bottomrow = 0
	tree = graph(treefile_path)

	def __init__(self):
		self.root.geometry("1270x720")
		self.auto_configure()

	def auto_configure(self):
		self.frame = tk.Frame(self.canvas)
		self.canvas.place(x=0,y=0,width=1920,height=720)
		self.canvas.create_window((0,0), window=self.frame, anchor=tk.NW, width=720)
		self.bar.pack(side=tk.RIGHT, fill=tk.Y)
		self.bar.config(command=self.canvas.yview)
		self.canvas.config(scrollregion=(0,0,0,200*15))
		self.canvas.config(yscrollcommand=self.bar.set)

	def set_images(self):
		for i in range(len(self.tree.nodes)):
			fig = Image.open(dbdir_path+self.tree.nodes[i])
			fig = fig.resize(size=(100,100))
			self.img[self.tree.nodes[i]] = ImageTk.PhotoImage(fig)

	def set_path(self):
		print(self.tree.path)
		for name in self.tree.path:
			tk.Label(self.frame, image=self.img[name]).grid(column=0,row=self.bottomrow)
			self.bottomrow+=1

	def set_candidates(self):
		for i in self.tree.next(self.tree.path[-1]):
			tk.Label(self.frame, image=self.img[i]).grid(column=0,row=self.bottomrow)
			tk.Button(self.frame, text='apply', command=lambda: self.button_pressed(i)).grid(column=1,row=self.bottomrow)
			self.bottomrow+=1

	def button_pressed(self, appended_node):
		self.tree.path.append(appended_node)
		self.canvas_reset()
		self.set_path()
		self.set_candidates()

	def canvas_reset(self):
		self.frame.destroy()
		self.auto_configure()
		self.bottomrow = 0

def main():
	hoge = app()
	hoge.set_images()
	hoge.set_path()
	hoge.set_candidates()
	hoge.root.mainloop()

if __name__ == '__main__':
	main()
