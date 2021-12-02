#!/usr/bin/env python3
import graph
import pygame
import sys
import math

DBpath = 'DBfigures/'
DBallpics = DBpath+'allpics.txt'
DBfile = DBpath+'graph.txt'
root = 'fig1.png'

def distance(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

class app:
	screen_size = (1280,720)
	image_size = 200
	background = 0,0,0
	images = {}
	imagepos = {}
	zero = (0, 0)
	def __init__(self):
		self.tree = graph.graph(DBfile, root)
		pygame.init()
		self.screen = pygame.display.set_mode(self.screen_size)
		pygame.display.set_caption('membrane transition')
		self.loadimages()
		pygame.display.flip()
		pygame.key.set_repeat(50)

	def loadimages(self):
		all = open(DBallpics).read().split('\n')
		for line in all[:-1]:
			self.images[line] = pygame.image.load(DBpath+line)
			self.images[line] = pygame.transform.scale(self.images[line],(self.image_size,self.image_size))
			self.imagepos[line] = self.images[line].get_rect()
			# self.screen.blit(self.images[line], self.imagepos[line])

	def setpath(self):
		for i in range(len(self.tree.path)):
			self.imagepos[self.tree.path[i]].x = self.zero[0]
			self.imagepos[self.tree.path[i]].y = self.imagepos[self.tree.path[i]].height*i+self.zero[1]
			self.screen.blit(self.images[self.tree.path[i]], self.imagepos[self.tree.path[i]])

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
			if ispressed:
				self.tree.path.append(candidates[min_idx].dst)
		else:
			self.screen.blit(self.images[image], self.imagepos[image])

	def draw(self):
		self.screen.fill(self.background)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == 106: # j, scroll down
					self.zero = (self.zero[0], self.zero[1]-10)
				elif event.key == 107: # k, scroll up
					self.zero = (self.zero[0], self.zero[1]+10)
				elif event.key == 113: # q, quit
					sys.exit()
		self.setpath()
		mousepos = pygame.mouse.get_pos()
		ispressed = pygame.mouse.get_pressed()
		self.replace_selected(mousepos, self.tree.path[-1], ispressed[0])
		pygame.display.flip()

def main():
	hoge = app()
	while True: hoge.draw()

if __name__ == '__main__':
	main()
