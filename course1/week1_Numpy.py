# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 17:00:01 2018

@author: TomotaY
"""
import numpy as np

x = np.array([1,2,3])
print(x)

y = np.array([4,5,6])

m = np.array([[7,8,9],[10,11,12]])

# dimensions of the array
m.shape

# 連続値をつくつる　０から３０まで２飛ばし
n = np.arange(0,30,2)

#arrayのshapeを変える
n = n.reshape(3,5)

# 連続値をつくる　０から４まで９個に区切る
o= np.linspace(0,4,9)

o.resize(3,3)

#arrayをつくる
np.ones((3,2))
np.zeros((2,3))
np.eye(3)

#!catはwindowsでは動かない
import os  
os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/course1")
 
 

