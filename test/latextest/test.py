#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

matplotlib.rcParams.update({'text.usetex': True})
matplotlib.rc('text.latex', preamble=r"\usepackage{xcolor}")

plt.grid(False)
fig, ax = plt.subplots(figsize=(15,1.1), dpi=50)
ax.axis("off")
a = r'$S_0: M^{+}m^{+}M^{+}m^{+}M^{+}\textcolor{red}{m^{+}}M^{+}m^{+}$'
plt.text(x=-0.1,y=0.1,s=a, horizontalalignment='left', fontsize=50)
plt.savefig("hoge.eps")
tmp = Image.open("hoge.eps")
tmp.save("hoge.png")

# canvas = agg.FigureCanvasAgg(fig)
# canvas.draw()
# renderer = canvas.get_renderer()
# raw_data = renderer.tostring_rgb()

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((1200, 400))
screen = pygame.display.get_surface()

# size = canvas.get_width_height()

# surf = pygame.image.fromstring(raw_data, size, "RGB")
surf = pygame.image.load("hoge.png")
screen.fill((0,0,0))
screen.blit(surf, (0,20))
pygame.display.flip()

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
