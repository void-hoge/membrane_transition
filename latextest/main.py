#!/usr/bin/env python3
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

x = np.linspace(0, 2*np.pi, 21)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1-y2

fig, ax = plt.subplots()
ax.plot(x, y1, 'b.-')
ax.plot(x, y2, 'g,-.')
ax.plot(x, y3, 'r,-.')

fig.canvas.draw()
im = np.array(fig.canvas.renderer.buffer_rgba())
# im = np.array(fig.canvas.renderer._renderer) # matplotlibが3.1より前の場合

img = Image.fromarray(im)
img.show()
