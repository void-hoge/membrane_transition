#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

matplotlib.rcParams.update({'text.usetex': True})
matplotlib.rc('text.latex', preamble=r"\usepackage{xcolor}\usepackage{dashrule}")

plt.grid(False)
fig, ax = plt.subplots(figsize=(15,1.1), dpi=50)
ax.axis("off")
a = r'$S_0: M^{+}m^{+}M^{+}m^{+}M^{+}\textcolor{red}{m^{+}}M^{+}m^{+}$'
plt.text(x=-0.1,y=0.1,s=a, horizontalalignment='left', fontsize=50)
plt.savefig('hoge.eps')
psimage=Image.open('hoge.eps')
psimage.save("hoge.png")
