#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pygame

plt.grid(False)
fig, ax = plt.subplots(figsize=(2, 2), dpi=100)
ax.axis("off")
a = r'$a$'
plt.text(x=0,y=0,s=a,size=30)
plt.show()
hoge = fig.canvas.tostring_rgb()
size = fig.canvas.get_width_height()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
surf = pygame.image.frombuffer(hoge, (200,200), 'RGB')
screen.blit(surf, (0,0))
pygame.display.flip()
