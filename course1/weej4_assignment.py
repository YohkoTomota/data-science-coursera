# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:25:31 2019

@author: Yohko Tomota
"""
import os  
os.chdir("C:/Users/fukey/Documents/data-science-coursera/course1")
os.listdir()

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
    data = []
    with open('university_towns.txt') as csvfile:
        for line in csvfile:
            line = line[:-1]
            
            if line[-6:] == '[edit]':
                state = line[:-6]
            else :
                town = line.split(sep = ' ',maxsplit=1)[0]   
                data.append([state,town])
    
    ans = pd.DataFrame(data,columns = ['State','RegionName'] )    
    return ans
get_list_of_university_towns()


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    df = pd.read_excel('gdplev.xls', skiprows = 7)
    df = df[['Unnamed: 4','Unnamed: 5']]
    df.columns = ['Quarter','GDP']
    df = df.loc[212:].reset_index(drop= True)
    recession_start = []
    for i in range(len(df) - 4):
        if ((df.iloc[i][1] > df.iloc[i+1][1]) & (df.iloc[i+1][1] > df.iloc[i+2][1])):
            if(df.iloc[i-1][0] not in recession_start):
                recession_start.append(df.iloc[i][0])

    ans = recession_start[0]
    return ans

get_recession_start()


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    df = pd.read_excel('gdplev.xls', skiprows = 7)
    df = df[['Unnamed: 4','Unnamed: 6']]
    df.columns = ['Quarter','GDP']
    df = df.loc[212:].reset_index(drop= True)
    
    recession_end = []
    for i in range(len(df) - 4):
        if ((df.iloc[i][1] > df.iloc[i+1][1]) & \
            (df.iloc[i+1][1] < df.iloc[i+2][1]) &\
            (df.iloc[i+2][1] < df.iloc[i+3][1])):
            recession_end.append(df.iloc[i+2][0])

    ans = recession_end[1]
    
    return ans
    
#     return '2009q4'
get_recession_end()

def get_recession_bottom():
    df = pd.read_excel('gdplev.xls', skiprows = 7)
    df = df[['Unnamed: 4','Unnamed: 5']]
    df.columns = ['Quarter','GDP']
    df = df.set_index('Quarter')
     
    ans = df.loc[get_recession_start():get_recession_end()].GDP.idxmin()
     
    return ans
    
get_recession_bottom()



def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    df = pd.read_csv('City_Zhvi_AllHomes.csv', encoding='latin-1')
    df.State = df.State.apply(lambda x : states.get(x) or x)
    df = df.drop(df.columns[[0] + list(range(3,51))], axis=1)
    df.set_index(['State','RegionName'],inplace= True)
    df.head()

    df = df.groupby(pd.PeriodIndex(df.columns, freq='q'), axis=1).mean()

    df.columns = [ str(x).lower() for x in df.columns.tolist()  ]
    ans = df[df.columns[1:67]]
    return ans

convert_housing_data_to_quarters()
# convert_housing_data_to_quarters().loc["Texas"].loc["Austin"].loc["2010q3"]

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    unitowns = get_list_of_university_towns()
    start = get_recession_start()
   
    bottom = get_recession_bottom()
    hdata = convert_housing_data_to_quarters()
    
    bstart = hdata.columns[hdata.columns.get_loc(start) - 1]
    
    hdata['ratio'] =  hdata[bstart] - hdata[bottom]
    hdata = hdata[[bottom, bstart, 'ratio']]
    hdata = hdata.reset_index()
    
    unitowns_hdata = pd.merge(hdata,unitowns,how='inner',on=['State','RegionName'])
    unitowns_hdata['uni'] = True
    unitowns_hdata.dropna(inplace=True)
    unitowns_hdata.set_index(['State','RegionName'], inplace = True )

    non_unitowns_hdata = pd.merge(hdata, unitowns, on=['State','RegionName'], how='outer')
    non_unitowns_hdata['univ'] = False
    non_unitowns_hdata.dropna(inplace = True)
    non_unitowns_hdata.set_index(['State','RegionName'], inplace = True )
    non_unitowns_hdata.univ.value_counts()
        
    t,p = ttest_ind(unitowns_hdata.ratio, non_unitowns_hdata.ratio)
    different = True if p<0.01 else False
    better = "university town" if unitowns_hdata['ratio'].mean() < non_unitowns_hdata['ratio'].mean() else "non-university town"
    
    return(different, p, better)

run_ttest()

