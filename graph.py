#!/usr/bin/env python3
import sys

DBpath = '../DBfigures/'
DBfile = DBpath+'graph.txt'
root = 'fig1.png'

class edge:
	def __init__(self, dst, highlighted, x, y):
		self.dst = dst
		self.highlighted = highlighted
		self.x = x
		self.y = y
	def __repr__(self):
		return 'edge<dst: {}, highlighted: {}, (x, y):({}, {})>'.format(self.dst, self.highlighted, self.x, self.y)

class graph:
	def __init__(self, filepath, root):
		self.edge = {} # {src: [(dst, highlighted, x, y), (dst, highlighted, x, y)...], ...}
		self.node = set()
		self.path = list()
		all = open(filepath).read().split('\n')
		for line in all[:-1]:
			tmp = line.split()
			if tmp[0] not in self.edge:
				self.edge[tmp[0]] = []
			self.edge[tmp[0]].append(edge(tmp[1], tmp[2], float(tmp[3]), float(tmp[4])))
			self.node.add(tmp[0])
			self.node.add(tmp[1])
		self.path.append(root)
	def get_next(self):
		if self.path[-1] not in self.edge:
			return None
		return self.edge[self.path[-1]]

def main():
	tree = graph(DBfile, root)
	print(tree.get_next())

if __name__ == '__main__':
	main()
