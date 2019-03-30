# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:26:38 2019

@author: Yohko Tomota
"""

#learn plots
import matplotlib.pyplot as plt
import numpy as np

#jupyter case 
plt.figure()
plt.subplot(1,2,1)

linear_data = np.array([1,2,3,4,6,7,8,9])
plt.plot(l
         inear_data, '-o')
plt.plot(linear_data, '-x')
exponential_data = linear_data**2

plt.subplot(1,2,2)
plt.plot(exponential_data,'-o')

#normal environment
fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(linear_data, '-o')

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(exponential_data,'-x')

# show plots
fig.tight_layout()
fig.show()
