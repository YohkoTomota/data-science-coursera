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


#Formula for standard deviation
#$$\sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \overline{x})^2}$$

np.random.normal
np.random.binomial
np.random.uniform

import scipy.stats as stats
distribution = np.random.normal(0.75,size=1000)
np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))

#check distribution shape
stats.kurtosis(distribution)
stats.skew(distribution)

chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)

#Hyphothesis testing
df = pd.read_csv('grades.csv')
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']

from scipy import stats
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])


