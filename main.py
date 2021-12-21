#!/usr/bin/env python3
import graph
import render
import pygame
import sys
import math
from PIL import Image
import time

DBdir = 'DBfigures/'
DBallpics = DBdir+'allpics.txt'
DBfile = DBdir+'graph.txt'

def distance(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

class transition:
	def __init__(self):
		self.screen_size = (1280,720)
		self.image_size = 200
		self.background = (255,255,255)
		self.images = {}
		self.imagepos = {}
		self.formula = {}
		self.formulapos = {}
		self.rule = {}
		self.rulepos = {}
		self.zero = (0, 0)
		self.tree = graph.graph(DBfile)
		pygame.init()
		self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
		pygame.display.set_caption('membrane transition')
		self.loadimages()
		pygame.display.flip()

	def loadimages(self):
		all = open(DBallpics).read().split('\n')
		for line in all[:-1]:
			tmp = line.split();
			fig = tmp[0];
			fml = tmp[1];
			print("Loading {}, {}, {}".format(fig+'.png', fig+'_fml.png', fml))
			if 'rule_' in fig:
				# a rule
				self.rule[fml] = pygame.image.load(DBdir+fig+'_fml.png')
				self.rulepos[fml] = self.rule[fml].get_rect()
			else:
				# not a rule
				self.images[fig] = pygame.image.load(DBdir+fig+'.png')
				self.images[fig] = pygame.transform.scale(self.images[fig],(self.image_size,self.image_size))
				self.imagepos[fig] = self.images[fig].get_rect()
				self.formula[fig] = pygame.image.load(DBdir+fig+'_fml.png')
				self.formulapos[fig] = self.formula[fig].get_rect()
		print("All images and formulas were successfully loaded.")

	def setpath(self):
		for i in range(len(self.tree.path)):
			tmp = self.tree.path[i]
			self.imagepos[tmp].x = self.zero[0]
			self.imagepos[tmp].y = self.imagepos[tmp].height*i+self.zero[1]
			self.screen.blit(self.images[tmp], self.imagepos[tmp])
			self.formulapos[tmp].x = self.zero[0]+self.imagepos[tmp].width
			self.formulapos[tmp].y = self.imagepos[tmp].height*i+self.zero[1]
			self.screen.blit(self.formula[tmp], self.formulapos[tmp])
			if i >= 1:
				rule = self.tree.rule_path[i-1]
				self.rulepos[rule].x = self.zero[0]+self.imagepos[tmp].width
				self.rulepos[rule].y = self.zero[1]+self.imagepos[tmp].height*(i-1)+self.formulapos[tmp].height
				self.screen.blit(self.rule[rule], self.rulepos[rule])

	def is_selected(self, mousepos, image):
		imagepos = self.imagepos[image]
		if imagepos.x < mousepos[0] and imagepos.x+imagepos.width > mousepos[0]:
			if imagepos.y < mousepos[1] and imagepos.y+imagepos.height > mousepos[1]:
				return True
		return False

	def replace_selected(self, mousepos, image, ispressed):
		# show the highlighted which closest to the mousepos on selected the image
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
			self.rulepos[candidates[min_idx].rule].x = self.formulapos[self.tree.path[-1]].x
			self.rulepos[candidates[min_idx].rule].y = self.formulapos[self.tree.path[-1]].y + self.formulapos[self.tree.path[-1]].height
			self.screen.blit(self.rule[candidates[min_idx].rule], self.rulepos[candidates[min_idx].rule])
			if ispressed:
				self.tree.push_path(candidates[min_idx])
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
		self.replace_selected(mousepos, self.tree.path[-1], ispressed[0])
		pygame.display.flip()

def main():
	render.render(DBdir, DBallpics)
	hoge = transition()
	while True: hoge.draw()

if __name__ == '__main__':
	main()
