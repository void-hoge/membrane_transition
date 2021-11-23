#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(2, 2))
ax.axis("off")
# toolbar = plt.get_current_fig_manager().toolbar
# for x in toolbar.actions():
#     toolbar.removeAction(x)
plt.grid(False)
a = r'$a$'
plt.text(x=0,y=0,s=a,size=30)
plt.show()
