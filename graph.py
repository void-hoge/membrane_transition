#!/usr/bin/env python3
import sys

DBpath = './DBfigures/'
DBfile = DBpath+'graph.txt'
root = 'fig1'

class edge:
	def __init__(self, dst, highlighted, x, y, rule):
		self.dst = dst
		self.highlighted = highlighted
		self.x = x
		self.y = y
		self.rule = rule
	def __repr__(self):
		return 'edge<dst: {}, highlighted: {}, (x, y):({}, {}), rule:{}>'.format(self.dst, self.highlighted, self.x, self.y, self.rule)

class graph:
	def __init__(self, filepath):
		self.edge = {} # {src: [(dst, highlighted, x, y), (dst, highlighted, x, y)...], ...}
		self.node = set()
		self.path = list()
		self.rule_path = list()
		all = open(filepath).read().split('\n')
		self.root = all[0].split()[0]
		for line in all[:-1]:
			tmp = line.split()
			if tmp[0] not in self.edge:
				self.edge[tmp[0]] = []
			self.edge[tmp[0]].append(edge(tmp[1], tmp[2], float(tmp[3]), float(tmp[4]), tmp[5]))
			self.node.add(tmp[0])
			self.node.add(tmp[1])
		self.path.append(self.root)

	def get_next(self):
		if self.path[-1] not in self.edge:
			return None
		return self.edge[self.path[-1]]

	def reset(self):
		self.path = []
		self.path.append(self.root)

	def push_path(self, edg):
		if not isinstance(edg, edge):
			raise Exception("edg must be a instance of edge.")
		self.path.append(edg.dst)
		self.rule_path.append(edg.rule)

	def pop_path(self):
		if len(self.path) != 1:
			self.path.pop()
			self.rule_path.pop()

def main():
	tree = graph(DBfile)
	tree.push_path(tree.get_next()[0])
	print(tree.get_next())

if __name__ == '__main__':
	main()
