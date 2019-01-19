# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 08:22:32 2019

@author: TomotaY
"""
import os 
os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/course1")
import pandas as pd
import numpy as np

#http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64
df = pd.read_csv('cars.csv')
x1 = df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
x2 = df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)