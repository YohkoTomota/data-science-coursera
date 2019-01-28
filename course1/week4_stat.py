# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:46:57 2018

@author: TomotaY
"""

import os  
os.chdir("C:/Users/fukey/Documents/data-science-coursera/course1")
import pandas as pd
import numpy as np

x = np.random.binomial(20, .5, 10000)
print((x>=15).mean())
np.random.binomial(1000,0.5)/1000
