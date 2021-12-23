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
		self.formula_height = 80
		self.background = (255,255,255) # white
		self.image = {}
		self.formula = {}
		self.rule = {}
		self.zero = (0, 0) # origin point (it moves when scrolling)
		self.tree = graph.graph(DBfile)
		pygame.init()
		self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
		pygame.display.set_caption('membrane transition')
		self.loadimage()

	def loadimage(self):
		""" Load all images DBdir using DBallpics.
		If the file name starts with 'rule_', load the formula(rule) image into self.rule with the key as the formula.
		If not, load the figure into self.image and load the formula image self.formula with the key as the filename.
		"""
		all = open(DBallpics).read().split('\n')
		for line in all[:-1]:
			tmp = line.split();
			fig = tmp[0];
			fml = tmp[1];
			print("Loading {}, {}, {}".format(fig+'.png', fig+'_fml.png', fml), file=sys.stderr)
			if 'rule_' in fig:
				# a rule
				self.rule[fml] = pygame.image.load(DBdir+fig+'_fml.png')
				width = self.rule[fml].get_rect().width * (self.formula_height/self.rule[fml].get_rect().height)
				self.rule[fml] = pygame.transform.scale(self.rule[fml], (width, self.formula_height))
			else:
				# not a rule
				self.image[fig] = pygame.image.load(DBdir+fig+'.png')
				self.image[fig] = pygame.transform.scale(self.image[fig],(self.image_size,self.image_size))
				self.formula[fig] = pygame.image.load(DBdir+fig+'_fml.png')
				width = self.formula[fig].get_rect().width * (self.formula_height/self.formula[fig].get_rect().height)
				self.formula[fig] = pygame.transform.scale(self.formula[fig], (width, self.formula_height))
		print("All image and formulas were successfully loaded.", file=sys.stderr)

	def put_image(self, name, pos):
		""" Display the image in self.image named name in pos.
		"""
		self.screen.blit(self.image[name], pos)

	def put_formula(self, name, pos):
		""" Display the formula in self.formula named name in pos.
		"""
		self.screen.blit(self.formula[name], pos)

	def put_rule(self, name, pos):
		""" Display the rule in self.rule named name in pos.
		"""
		self.screen.blit(self.rule[name], pos)

	def setpath(self):
		""" Read path from self.tree and display it.
		Display highlited except for the newest (below) state.
		"""
		for i in range(len(self.tree.edge_path)):
			edg = self.tree.edge_path[i]
			# put highlighted images
			pos = (self.zero[0], self.zero[1] + self.image_size*i)
			self.put_image(edg.highlighted, pos)
			# put formulas
			pos = (self.zero[0]+self.image_size, self.zero[1] + self.image_size*i)
			self.put_formula(edg.highlighted, pos)
			# put rules
			pos = (self.zero[0]+self.image_size, self.zero[1] + self.image_size*i + self.formula_height)
			self.put_rule(edg.rule, pos)
		# plaec current image
		idx = len(self.tree.edge_path)
		back = self.tree.path[-1]
		pos = (self.zero[0], self.zero[1]+self.image_size*len(self.tree.edge_path))
		self.put_image(back, pos)

	def is_selected(self, mousepos, pos):
		"""Determine if there is a mouse in the image with pos in the upper left
		"""
		if pos[0] < mousepos[0] and pos[0]+self.image_size > mousepos[0]:
			if pos[1] < mousepos[1] and pos[1]+self.image_size > mousepos[1]:
				return True
		return False

	def replace_selected(self, mousepos, image, ispressed):
		""" When the mouse selects the image, replace it with the next transition image.
		"""
		replace_pos = (self.zero[0], self.zero[1]+self.image_size*len(self.tree.edge_path))
		if self.is_selected(mousepos, replace_pos):
			candidates = self.tree.get_next()
			if candidates == None: # if there is no edge from current state
				tmp_pos = (self.zero[0]+self.image_size, self.zero[1] + self.image_size*len(self.tree.edge_path))
				self.put_image(image, replace_pos)
				self.put_formula(image, tmp_pos)
				return
			dist = []
			for a in candidates:
				dist.append(distance(mousepos[0]-replace_pos[0], mousepos[1]-replace_pos[1], a.x*self.image_size, a.y*self.image_size))
			min = 10000
			min_idx = 0
			for i in range(len(dist)):
				if dist[i] < min:
					min = dist[i]
					min_idx = i
			self.put_image(candidates[min_idx].highlighted, replace_pos)
			tmp_pos = (self.zero[0] + self.image_size, self.zero[1]+self.image_size*len(self.tree.edge_path))
			self.put_formula(candidates[min_idx].highlighted, tmp_pos)
			tmp_pos = (self.zero[0] + self.image_size, self.zero[1] + self.image_size*len(self.tree.edge_path) + self.formula_height)
			self.put_rule(candidates[min_idx].rule, tmp_pos)
			if ispressed:
				self.tree.push_path(candidates[min_idx])
		else:
			tmp_pos = (self.zero[0] + self.image_size, self.zero[1] + self.image_size*len(self.tree.edge_path))
			self.put_image(image, replace_pos)
			self.put_formula(image, tmp_pos)

	def draw(self):
		""" main loop function
		"""
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
