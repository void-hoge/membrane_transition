#!/usr/bin/env python3
import graph
import pygame
import sys
import math
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import os

matplotlib.use("Agg")
matplotlib.rcParams.update({'text.usetex': True})
matplotlib.rc('text.latex', preamble=r"\usepackage{xcolor}")

DBpath = 'DBfigures/'
DBallpics = DBpath+'allpics.txt'
DBfile = DBpath+'graph.txt'
root = 'fig1.png'

def distance(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def tex2surface(str):
	plt.grid(False)
	fig, ax = plt.subplots(figsize=(20,1.1), dpi=50)
	ax.axis("off")
	plt.text(x=-0.1,y=0.1,s=str, horizontalalignment='left', fontsize=50)
	plt.savefig("tmp.eps")
	plt.close()
	tmp = Image.open("tmp.eps")
	tmp.save("tmp.png")
	surface = pygame.image.load("tmp.png")
	os.system("rm tmp.png")
	os.system("rm tmp.eps")
	return surface

class transition:
	screen_size = (1280,720)
	image_size = 200
	background = (255,255,255)
	images = {}
	imagepos = {}
	formula = {}
	formulapos = {}
	zero = (0, 0)
	def __init__(self):
		self.tree = graph.graph(DBfile, root)
		pygame.init()
		self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
		pygame.display.set_caption('membrane transition')
		self.loadimages()
		pygame.display.flip()
		# pygame.key.set_repeat(50)

	def loadimages(self):
		all = open(DBallpics).read().split('\n')
		for line in all[:-1]:
			tmp = line.split();
			fig = tmp[0];
			fml = tmp[1];
			print("Loading {}, {}".format(fig, fml))
			self.images[fig] = pygame.image.load(DBpath+fig)
			self.images[fig] = pygame.transform.scale(self.images[fig],(self.image_size,self.image_size))
			self.imagepos[fig] = self.images[fig].get_rect()
			self.formula[fig] = tex2surface(fml);
			self.formulapos[fig] = self.formula[fig].get_rect()
		print("All images and formulaes were successfully loaded.")

	def setpath(self):
		for i in range(len(self.tree.path)):
			tmp = self.tree.path[i]
			self.imagepos[tmp].x = self.zero[0]
			self.imagepos[tmp].y = self.imagepos[tmp].height*i+self.zero[1]
			self.screen.blit(self.images[tmp], self.imagepos[tmp])
			self.formulapos[tmp].x = self.zero[0]+self.imagepos[tmp].width
			self.formulapos[tmp].y = self.imagepos[tmp].height*i+self.zero[1]
			self.screen.blit(self.formula[tmp], self.formulapos[tmp])

	def is_selected(self, mousepos, image):
		imagepos = self.imagepos[image]
		if imagepos.x < mousepos[0] and imagepos.x+imagepos.width > mousepos[0]:
			if imagepos.y < mousepos[1] and imagepos.y+imagepos.height > mousepos[1]:
				return True
		return False

	def replace_selected(self, mousepos, image, ispressed):
		# show the highlighted closest to the mousepos on selected the image
		imagepos = self.imagepos[image]
		if self.is_selected(mousepos, image):
			candidates = self.tree.get_next()
			if candidates == None:
				return
			dist = []
			for a in candidates:
				dist.append(distance(mousepos[0]-imagepos[0], mousepos[1]-imagepos[1], a.x*self.image_size, a.y*self.image_size))
			min = self.image_size*self.image_size
			min_idx = 0
			for i in range(len(dist)):
				if dist[i] < min:
					min = dist[i]
					min_idx = i
			self.imagepos[candidates[min_idx].highlighted] = self.imagepos[image]
			self.screen.blit(self.images[candidates[min_idx].highlighted], self.imagepos[candidates[min_idx].highlighted])
			self.screen.blit(self.formula[candidates[min_idx].highlighted], self.formulapos[self.tree.path[-1]])
			if ispressed:
				self.tree.path.append(candidates[min_idx].dst)
		else:
			self.screen.blit(self.images[image], self.imagepos[image])
			self.screen.blit(self.formula[image],self.formulapos[image])

	def draw(self):
		self.screen.fill(self.background)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == ord('j'): # j, scroll down
					self.zero = (self.zero[0], self.zero[1]-10)
				elif event.key == ord('k'): # k, scroll up
					self.zero = (self.zero[0], self.zero[1]+10)
				elif event.key == ord('h'): # h, scroll left
					self.zero = (self.zero[0]-10, self.zero[1])
				elif event.key == ord('l'): # l, scroll right
					self.zero = (self.zero[0]+10, self.zero[1])
				elif event.key == ord('r'): # r, reset
					self.tree.reset()
				elif event.key == ord('u'): # u, undo
					self.tree.pop_path()
				elif event.key == ord('q'): # q, quit
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					self.zero = (self.zero[0], self.zero[1]+20)
				if event.button == 5:
					self.zero = (self.zero[0], self.zero[1]-20)
		self.setpath()
		mousepos = pygame.mouse.get_pos()
		ispressed = pygame.mouse.get_pressed()
		# print(len(self.tree.path))
		self.replace_selected(mousepos, self.tree.path[-1], ispressed[0])
		pygame.display.flip()

def main():
	hoge = transition()
	while True: hoge.draw()

if __name__ == '__main__':
	main()
