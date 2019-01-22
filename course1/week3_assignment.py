# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:16:13 2019

@author: TomotaY
"""

import os
os.chdir("C:/Users/fukey/Documents/dara-sciensce-cursera/course1")

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
 
energy = pd.read_excel('Energy Indicators.xls', sheet_name='Energy' ,
                   skiprows=9, skipfooter = 38 )
energy = energy.drop(index= list(range(8)), columns=['Unnamed: 0','Unnamed: 1'])
energy = energy.loc[energy.index.notnull()]
#list(df) ---get colname 
energy = energy.rename( columns={"Country": "Country", 
                              "Energy Supply": "Energy Supply",
                              "Energy Supply per capita":"Energy Supply per Capita",
                              "Renewable Electricity Production":"% Renewable"})
energy = energy.replace('...', np.NaN)
#Rename several country
di = {"Republic of Korea": "South Korea",
                  "United States of America": "United States",
                  "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                  "China, Hong Kong Special Administrative Region": "Hong Kong"}
#doesn't work: df["Country"].replace(di,inplace = True)
energy = energy.replace({"Country": di})
#remove parenthesis
energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
energy['Energy Supply']*=1000000

#load the GDP data from the file world_bank.csv
GDP = pd.read_csv('world_bank.csv',skiprows=4)
#len(GDP) ---check row number
di = {"Korea, Rep.": "South Korea", 
      "Iran, Islamic Rep.": "Iran",
      "Hong Kong SAR, China": "Hong Kong"}
GDP = GDP.replace({'Country Name': di})
#col = ['Country Name'] + list(range(2006,2016))
col = ['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
GDP = GDP[col]
GDP = GDP.rename(columns={"Country Name": "Country"}) 

ScimEn = pd.read_excel('scimagojr-3.xlsx')
#ScimEn = ScimEn.where(ScimEn['Rank']<16).dropna()
ScimEn_top15 = ScimEn.loc[:14]

#merge_inner
df = pd.merge(ScimEn_top15 , energy, how = 'left', left_on = 'Country', right_on = 'Country')
df = pd.merge(df, GDP, how = 'left', left_on = 'Country', right_on = 'Country')

df = df.set_index('Country')

#merge_outer
df2 = pd.merge(ScimEn, energy, how = 'outer', left_on = 'Country', right_on = 'Country')
df2 = pd.merge(df2, GDP, how = 'outer', left_on = 'Country', right_on = 'Country')
