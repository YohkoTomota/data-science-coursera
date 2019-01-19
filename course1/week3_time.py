# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 08:44:34 2019

@author: TomotaY
"""

import pandas as pd
import numpy as np

#Timestamp
pd.Timestamp('1/1/2019 8:45AM')
#Period
pd.Period('1/2019')
pd.Period('1/1/2019')

#Datetime index
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
#Period index
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])

#Converting to Datetime
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
ts3.index = pd.to_datetime(ts3.index)
#format
pd.to_datetime('4.7.12', dayfirst=True)

#Time diff
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')
pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')

#dates in dateframe
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
#weekday
df.index.weekday_name

#first row base diff
df.diff()

#mean for each month
df.resample('M').mean()


#quary date data
df['2017']
df['2016-12':]

df.asfreq('W', method='ffill')
import matplotlib.pyplot as plt

df.plot()

