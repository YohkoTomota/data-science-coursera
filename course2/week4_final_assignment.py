# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Mannheim, Baden-Württemberg Region, Germany**, or **Germany** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Mannheim, Baden-Württemberg Region, Germany** to Ann Arbor, USA. In that case at least one source file must be about **Mannheim, Baden-Württemberg Region, Germany**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Mannheim, Baden-Württemberg Region, Germany** and **religious events or traditions**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)


#For this assignment I choosed thema German religion and refugee for each bundeslands.

#data source is available here 
#Germany :
#https://zacat.gesis.org/webview/index.jsp?headers=http%3A%2F%2F193.175.238.79%3A80%2Fobj%2FfVariable%2FZA6888_V313&stubs=http%3A%2F%2F193.175.238.79%3A80%2Fobj%2FfVariable%2FZA6888_V7&previousmode=table&sort=column&byc=2&study=http%3A%2F%2F193.175.238.79%3A80%2Fobj%2FfStudy%2FZA6888&charttype=null&by=1&mode=table&v=2&V313slice=1&V7slice=12&order=asc&weights=http%3A%2F%2F193.175.238.79%3A80%2Fobj%2FfVariable%2FZA6888_V319&weights=http%3A%2F%2F193.175.238.79%3A80%2Fobj%2FfVariable%2FZA6888_V320&analysismode=table&gs=5&tabcontenttype=row&top=yes#https://www.brookings.edu/research/cities-and-refugees-the-german-experience/
#Japan :
#https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00401101&tstat=000001018471&cycle=0&tclass1=000001094555#http://www.eurocities.eu/eurocities/documents/Refugee-reception-and-integration-in-cities-WSPO-A8KCQ5

#Baden-Württemberg, Germany, Religion 

#in germany, there are 16 bundesland (state). It is known that there is still cultual differencec between east and west part.
#Does the religion also differ for each bundesland?
#and what about my home country, Japan ? 
# 

#Summary
#The right graph shows religion in germany according to the censuses. Like as other europian countries,
#Christian is most biggest religion in Germany. A clear feature can be observed between
#east and west part, in terms of Catholic population. in all east part and Schleswig-Holstein(located in north-east)
#catholic is very small whereas protestant is majolity.

#Compare to Japan, there is no clear dependency on area. Basically people are resisterd as temple or shrine
#which his/her family belongs to. And most of people does not intensionaly leave them because there is 
#no obrigation nor tax to be with. This seems the reason that there is no area dependency.



Basically population of east is less than that of west but 


import os
os.chdir('C:\\Users\\TomotaY\\OneDrive - BASF\\Documents\\Coursera/data-science-coursera/course2')
print (__file__)

# religion = open('./german_religion.csv')
# data = csv.reader(religion,delimiter=",")

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("./german_religion.xlsx", encoding="utf-8",  sep=",")

data = data.set_index("Bundesland")

data.columns = ['Catholic_r', 'Protestant_r','Muslim_r','Judaism_r','Others_r','NoReligion_r','Total_r','N']

# Plot ratio within bundesland
data_ratio = data.drop(['Total_r','N'], axis=1)

ax = data_ratio.plot(kind="barh", stacked=True, use_index = True)
ax.set(xlabel="Ratio")
#print(type(ax))
#plt.show()



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





