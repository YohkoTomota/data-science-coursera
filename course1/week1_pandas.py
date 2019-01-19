# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:17:15 2018

@author: TomotaY
"""

import pandas as pd

#pd.Series?
animals = ['Tiger','Bear','Moose']
pd.Series(animals)

animals = ['Tiger','Bear', None]
pd.Series(animals)

#NaN に注意

sports = {'Archery' : 'Shutan',
          'Golf' : 'Scotland',
          'Sumo' : 'Japan',
          'Taekwando' : 'Korea'}

s = pd.Series(sports)
s

#iloc and loc are more specificなのでおすすめ
s.iloc[2]
s[2]

s.loc['Golf']
s['Golf']

sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)




s = pd.Series([100.00, 120.00, 101.00, 3.00])
#basic loop
total = 0 
for item in s:
    total +=item
print(total)

#GYOU-RETSU niha numpy
import numpy as np
total = np.sum(s)

#craete random numbers
s = pd.Series(np.random.randint(0,1000,10000))

s+=2

#functionirert night
for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()


#data frame#################BASIC
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()

df.loc['Store 2']
df.T
df.T.loc['Cost']

df.loc['Store 1']['Cost']

df.loc[:,['Name', 'Cost']]

df.drop('Store 1')

#copy
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df
