# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:43:51 2019

@author: TomotaY
"""
#Reading 
#http://www.aosabook.org/en/matplotlib.html

import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(0,10,100)
b = np.exp(a)
plt.plot(a,b)
plt.show()

#backlayer
def on_press(event):
    if event.inaxes is None: return
    for line in event.inaxes.lines:
        if event.key=='t':
            visible = line.get_visible()
            line.set_visible(not visible)
    event.inaxes.figure.canvas.draw()

fig, ax = plt.subplots(1)

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(2, 20))

plt.show()
