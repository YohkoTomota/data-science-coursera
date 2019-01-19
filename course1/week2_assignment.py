# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:32:17 2018

@author: TomotaY
"""
import os  
os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/course1")
 

import pandas as pd

#Part1
#imposrt data 
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

#Which country has won the most gold medals in summer games?
def answer_one():
    df_summer = df[df['Gold'] == max(df['Gold'])]              
    return list(df_summer.index)[0]

#Which country had the biggest difference between their summer and winter gold medal counts?
def answer_two():
    df['dif'] = abs(df['Gold']-df['Gold.1'])
    df_dif = df[df['dif'] == max(df['dif'])]              
    return list(df_dif.index)[0]

#Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
import numpy as np
def answer_three():
     df['ref_dif'] =np.where((df['Gold'] !=0) & (df['Gold.1'] !=0), abs(df['Gold']-df['Gold.1'])/df['Gold.2'], 0)
     df_dif = df[df['ref_dif'] == max(df['ref_dif'])]              
     return list(df_dif.index)[0]

def answer_four():
    df['Point'] = df['Gold.2']*3 + df['Silver.2']*3 + df['Bronze.2']
    return df['Point']

#Part2 
#import data
census_df = pd.read_csv('census.csv')
census_df.head()
def answer_five():
    census_df_sd = census_df.loc[:,['STNAME','CTYNAME']]
    top = census_df_sd.groupby(['STNAME']).count().sort_values('CTYNAME', ascending=False).index[0]
    return top

def answer_six():
    #Grouped by stats, sort by CENSUS2010POP, sum up top 3 CENSUS2010POP.
    census_df_sd = census_df[census_df['SUMLEV'] == 50]
    census_df_sd = census_df_sd.loc[:,['STNAME','CENSUS2010POP']]
    census_df_sd = census_df_sd.groupby(['STNAME']).apply(lambda x: (x
                                       .sort_values('CENSUS2010POP', ascending=False)
                                       .head(3)
                                       .sum()))
    census_sm = list(census_df_sd.sort_values('CENSUS2010POP', ascending=False).head(3).index)
    return census_sm

#most boratile poplation
#POPESTIMATE2010-2015'
def answer_seven():
    census_df_sd = census_df[census_df['SUMLEV'] == 50]
    census_df_sd = census_df_sd.loc[:,['CTYNAME','POPESTIMATE2010','POPESTIMATE2011',
                                    'POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
    census_df_sd['dif'] = (census_df_sd.max(axis=1)-census_df_sd.min(axis=1))
    df_dif = census_df_sd[census_df_sd['dif'] == max(census_df_sd['dif'])]['CTYNAME']
    return list(df_dif)[0]

#Specific data extraction
def answer_eight():
    census_df_sd = census_df[(census_df['REGION'] == 1)  |(census_df['REGION'] == 2)]
    census_df_sd = census_df_sd[census_df_sd['CTYNAME'].str.contains('Washington')]
    census_df_sd = census_df_sd[census_df_sd['POPESTIMATE2015'] > census_df_sd['POPESTIMATE2014']][['STNAME','CTYNAME']]
    return census_df_sd