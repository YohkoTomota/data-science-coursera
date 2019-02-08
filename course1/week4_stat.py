# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:46:57 2018

@author: TomotaY
"""

import os  
#os.chdir("C:/Users/fukey/Documents/data-science-coursera/course1")
os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/data-science-coursera/course1")

import pandas as pd
import numpy as np

np.random.uniform(0, 1)
np.random.normal(0.75)


from scipy.stats import ttest_in


x = np.random.binomial(20, .5, 10000)
print((x>=15).mean())
np.random.binomial(1000,0.5)/1000



#Assignment
# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
#  '''Returns a DataFrame of towns and the states they are in from the 
#    university_towns.txt list. The format of the DataFrame should be:
#    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
#    columns=["State", "RegionName"]  )
#    
#    The following cleaning needs to be done:
#
#    1. For "State", removing characters from "[" to the end.
#    2. For "RegionName", when applicable, removing every character from " (" to the end.
#    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
#  
df = pd.read_csv('university_towns.txt', header = None, sep ='\n', error_bad_lines=False)
state = []
for index, row in df.iterrows():
    
    
with open('university_towns.txt') as file:
    data = []
    for line in file:
        data.append(line[:-1])

state_town = []
        
for line in data:
    if line[-6:] == '[edit]':
        state = line[:-6]
    elif '(' in line:
        town = line[:line.index('(')-1]
        state_town.append([state,town])
    else:
        town = line
        state_town.append([state,town])
   state_college_df = pd.DataFrame(state_town,columns = ['State','RegionName'])
  