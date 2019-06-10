# # Assignment 4


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("./german_religion.xlsx", encoding="utf-8",  sep=",")

data = data.set_index("Bundesland")

data.columns = ['Catholic_r', 'Protestant_r','Muslim_r','Judaism_r','Others_r','NoReligion_r','Total_r','N']

# Plot ratio within bundesland
data_ratio = data.drop(['Total_r','N'], axis=1)

ax = data_ratio.plot(kind="barh", stacked=True, use_index = True)
ax.set(xlabel="Ratio")

# add columns as pandas.Series 
data['Catholic'] = data['Catholic_r'] * data['N'] /100/1000
data['Protestant'] = data['Protestant_r'] * data['N'] /100/1000
data['Muslim'] = data['Muslim_r'] * data['N'] /100/1000
data['Judaism'] = data['Judaism_r'] * data['N'] /100/1000
data['Others'] = data['Others_r'] * data['N'] /100/1000

# Fig.1 populatino of each religion at each bundesland
data_abs = data[['Catholic', 'Protestant','Muslim','Judaism','Others']]
data_abs = data_abs.drop(['Total'], axis=0)

#to freistaat are involed into stadt.
#Hamburg => Schleswig-Holstein
#Bremen => Niedersachsen
#Berlin => Beandenburg
data_abs = data_abs.reset_index()

data_abs = data_abs.replace(regex = {'Hamburg' : "Schleswig-Holstein",  'Berlin-Ost' : "Brandenburg",  'Berlin-West' : "Brandenburg",'Bremen' : "Niedersachsen"})

data_abs = data_abs.groupby('Bundesland').sum()
#second index for East /West (Mecken, brandenburg, Saxony-anhalt, Saxomy, Thuringia)
data_abs['Region'] = ['west','west','east','west','east','west','west','west','west','east','east','west','east']
data_abs = data_abs.set_index('Region', append= True)
data_abs = data_abs.sort_index(level=1, sort_remaining=False)


bx = data_abs.plot(kind="barh", stacked=True, use_index = True)
bx.set(xlabel="People")
#plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
plt.savefig('German.png')


# japan data
### header = None : to get empty colmuns
data_jp = pd.read_excel("./japan_religion.xls", encoding="utf-8", sep=",")
data_jp = data_jp.reset_index()
### deleat 'total' row
data_jp = data_jp.drop(index = 0 ,axis =1)
data_jp.columns = ['Prefecture','Region','Shinto', 'Buddist','Catholic','Others','Total']

# Prefecture is too small -- group by region
data_jp = data_jp.groupby('Region').sum()
data_jp['Region'] = ['east','west','east','west','east','west','west','east']
data_jp = data_jp.set_index('Region', append =True)

jp_ratio = pd.DataFrame()
# ratio columns
jp_ratio['Shinto'] = data_jp['Shinto'] / data_jp['Total'] *100
jp_ratio['Buddist'] = data_jp['Buddist'] / data_jp['Total'] *100
jp_ratio['Catholic'] = data_jp['Catholic'] / data_jp['Total'] *100
jp_ratio['Others'] = data_jp['Others'] / data_jp['Total'] *100

ax = jp_ratio.plot(kind="barh", stacked=True, use_index = True)
ax.set(xlabel="Ratio")


jp_abs = data_jp.drop('Total', axis=1) 
jp_abs = jp_abs.sort_index(level=1)
bx = jp_abs.plot(kind="barh", stacked=True, use_index = True)
bx.set(xlabel="Peope")
#plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
plt.savefig('Japan.png')





