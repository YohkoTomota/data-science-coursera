# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 07:56:30 2019

@author: TomotaY
"""
import os 
os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/course1")
import pandas as pd
import numpy as np

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
#Category ordering
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
grades > 'C'

#series でも
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)


df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
#num をcategory にするためにcut を使ってbin=10で区切る
pd.cut(df['avg'],10)

#add labels
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])

