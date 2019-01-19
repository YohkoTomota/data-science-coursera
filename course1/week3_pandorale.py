# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 09:23:52 2018

@author: TomotaY
"""
import os 
os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/course1")
import pandas as pd
df = pd.read_csv('census.csv')

#good
(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns= {'ESTIMATESBASE2010': 'Estimates Base 2010'}))
#do same thing
df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})


#各列に対して処理。min,maxのみのデータをかえす
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})
df.apply(min_max, axis=1)

 #各列に対して処理。min,maxをdeata frameに追加
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
df.apply(min_max, axis=1)

 #lambdaは美しい
rows = ['POPESTIMATE2010',
         'POPESTIMATE2011',
         'POPESTIMATE2012',
         'POPESTIMATE2013',
         'POPESTIMATE2014',
         'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)