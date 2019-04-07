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

<<<<<<< HEAD
=======
np.random.uniform(0, 1)
np.random.normal(0.75)


from scipy.stats import ttest_in

>>>>>>> 1184bcc9260be680121c9d9c4c46440af7c3a32c

x = np.random.binomial(20, .5, 10000)
print((x>=15).mean())
np.random.binomial(1000,0.5)/1000


<<<<<<< HEAD
#Formula for standard deviation
#$$\sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \overline{x})^2}$$

np.random.normal
np.random.binomial
np.random.uniform

import scipy.stats as stats
distribution = np.random.normal(0.75,size=1000)
np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))

#check distribution shape
stats.kurtosis(distribution)
stats.skew(distribution)

chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)

#Hyphothesis testing
df = pd.read_csv('grades.csv')
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']

from scipy import stats
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])


=======

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
  
>>>>>>> 1184bcc9260be680121c9d9c4c46440af7c3a32c
