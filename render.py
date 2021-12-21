#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import os

matplotlib.use("Agg")
matplotlib.rcParams.update({'text.usetex': True})
matplotlib.rc('text.latex', preamble=r"\usepackage{xcolor}")

def render(dbdir, file):
	data = open(file).read().split('\n')
	try:
		prev = open('prev.txt').read().split('\n')
	except Exception as e:
		pass
	for i in range(len(data[:-1])):
		try:
			if data[i] in prev:
				continue
		except Exception as e:
			pass
		print("Rendering {}".format(data[i]))
		tmp = data[i].split()
		name = tmp[0]
		formula = tmp[1]
		plt.grid(False)
		fig, ax = plt.subplots(figsize=(20,1.1), dpi=50)
		ax.axis("off")
		plt.text(x=-0.1,y=0.1,s=formula, horizontalalignment='left', fontsize=50)
		plt.savefig("tmp.eps")
		plt.close()
		tmp = Image.open("tmp.eps")
		tmp.save(dbdir+name+'_fml.png')
		os.system("rm tmp.eps")
	prevfile = open('prev.txt', 'w')
	prevfile.write(open(file).read())
	prevfile.close()

def main():
	dbdir = 'DBfigures/'
	file = 'DBfigures/allpics.txt'
	render(dbdir, file)

if __name__ == '__main__':
	main()
