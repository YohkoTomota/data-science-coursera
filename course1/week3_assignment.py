# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:16:13 2019

@author: TomotaY
"""

import os
os.chdir("C:/Users/fukey/Documents/data-science-coursera/course1")

import pandas as pd
import numpy as np
 
energy = pd.read_excel('Energy Indicators.xls', sheet_name='Energy' ,
                   skiprows=17, skipfooter = 38 )
energy = energy[[ 'Unnamed: 2', 'Petajoules', 'Gigajoules', '%']]
energy = energy.loc[energy.index.notnull()]
#list(df) ---get colname 
energy = energy.rename( columns={'Unnamed: 2': "Country", 
                              'Petajoules': "Energy Supply",
                              'Gigajoules':"Energy Supply per Capita",
                              '%':"% Renewable"})
energy = energy.replace('...', np.NaN)
#remove parenthesis
energy['Country'] = energy['Country'].str.replace(" \(.*\)","")
#remove number
energy['Country'] = energy['Country'].str.replace("[0-9]","")

#Rename several country
di = {"Republic of Korea": "South Korea",
      "United States of America": "United States",
      "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
      "China, Hong Kong Special Administrative Region": "Hong Kong"}
#doesn't work: df["Country"].replace(di,inplace = True)
energy = energy.replace({"Country": di})

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
Top15 = df
#################################S
#The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
#merge_inner
df = pd.merge(ScimEn , energy, how = 'inner', left_on = 'Country', right_on = 'Country')
df = pd.merge(df, GDP, how = 'inner', left_on = 'Country', right_on = 'Country')
#merge_outer
df2 = pd.merge(ScimEn, energy, how = 'outer', left_on = 'Country', right_on = 'Country')
df2 = pd.merge(df2, GDP, how = 'outer', left_on = 'Country', right_on = 'Country')

print(len(df2)-len(df))
#################################
#What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
avgGDP = Top15[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']].mean(axis=1)
avgGDP.sort_values(ascending=False, inplace=True)

#################################
n6 =Top15[Top15.index=='Brazil']
n6.iloc[0]['2015'] - n6.iloc[0]['2006']
#################################
#What is the mean Energy Supply per Capita?
Top15.mean(0)['Energy Supply per Capita']
#What country has the maximum % Renewable and what is the percentage?
x = Top15[Top15['% Renewable']==Top15.max(0)['% Renewable']]
ans = (x.iloc[0].name,x.iloc[0]['% Renewable'])
#ratio of citation
Top15 = Top15.assign(cit_ratio=Top15['Self-citations']/Top15['Citations'])
x = Top15[Top15['cit_ratio']==Top15.max(0)['cit_ratio']]
ans = (x.iloc[0].name,x.iloc[0]['cit_ratio'])
#estimates the population using Energy Supply and Energy Supply per capita
Top15 = Top15.assign(est_popul=Top15['Energy Supply']/Top15['Energy Supply per Capita'])
x = Top15[Top15['est_popul']==Top15.max(0)['est_popul']].index
ans = x.iloc[0].name
#estimates the number of citable documents per person. 
Top15 = Top15.assign(est_citabledoc=Top15['Citable documents']/Top15['est_popul'])
#What is the correlation between the number of citable documents per capita and the energy supply per capita? 
#Use the .corr() method, (Pearson's correlation).
ans = Top15['est_citabledoc'].corr(Top15['Energy Supply per Capita'])
#################################
#Add column conditionally 
med = Top15.median(0)['% Renewable']
Top15 = Top15.assign(HeighRenew = [1 if x > med else 0 for  x in Top15['% Renewable']]) 
ans = Top15['HeighRenew']
ans = pd.Series(ans)
#################################
#Classify conti
ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
Top15 = Top15.reset_index()
Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
Top15 = Top15.assign(est_popul=Top15['Energy Supply']/Top15['Energy Supply per Capita'])
Top15.groupby('Continent')['est_popul'].agg(['size','sum','mean','std'])
#cut bin
Top15['bins'] = pd.cut(Top15['% Renewable'],5)
ans = Top15.groupby(['Continent', 'bins']).size()

#Convert the Population Estimate series to a string with thousands separator 
#(using commas). Do not round the results.
tmp = Top15['est_popul'].tolist()
PopEst= (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).apply(lambda x: "{:,}".format(x), tmp)
    


df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
#https://github.com/Qian-Han/coursera-Applied-Data-Science-with-Python