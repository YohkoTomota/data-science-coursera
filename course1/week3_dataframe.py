# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 08:53:20 2018

@author: TomotaY
"""

#Dataframe
import pandas as pd
df = pd.DataFrame([{'Name':'Chris', 'Item' : "Sponge", 'Cost':222.5},
                   {'Name':'Kevyn', 'Item' : "Kitty", 'Cost':223},
                   {'Name':'Filip', 'Item' : "Spoon", 'Cost':24}],
                   index = ['Store1','Store2', 'Store3'])

#add colums
df['Date'] = ['December 1','January 1', 'mid-May']

df['Delivered'] = True

df['Feedback'] = ['Positive',None,'Negative']

adf = df.reset_index() #index -> colmun にする

adf['Date'] = pd.Series({0: 'December 1', 2 :'mid-May'}) #missing valueはNaNで補完される

#Marge dataframes
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')  #column -> index にする

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

#index を使って　merge. 'how' to merge
pd.merge(staff_df, student_df, how = 'outer', left_index = True, right_index = True)
pd.merge(staff_df, student_df, how = 'inner', left_index = True, right_index = True)
pd.merge(staff_df, student_df, how = 'left', left_index = True, right_index = True)
pd.merge(staff_df, student_df, how = 'right', left_index = True, right_index = True)

#colnameを使ってmerge
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df,student_df, how = 'left', left_on = 'Name', right_on = 'Name')


staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
#複数カラムでmerge
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])