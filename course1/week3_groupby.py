# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 07:00:25 2019

@author: TomotaY
"""

import os 
os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/course1")
import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df

#calculate ave in sub group
for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + 'have an average population of '+ str(avg)) #number needs to be conv to str
    
#same thing using dataframe group by
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + 'have an average population of '+ str(avg)) #number needs to be conv to str

#grouping に function　を使う
df = df.set_index('STNAME') #groupby したいcolをindexに
def fun(item):  #よくわからん
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are '+ str(len(frame))+ 'records in group' + str(group))
    
#agg
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity')

#there is "dataframe groupby" and "series groupby" 
print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))
#dataframeGroup
x1 = (df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'] #group by index using level
    .agg({'avg': np.average, 'sum': np.sum}))
x1.head()
#SeriesGroup ---this case same
x2 = (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}))
x2.head()
#if pass name of dictionaly key same col name, be careful
x3 = (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))
x3.head()