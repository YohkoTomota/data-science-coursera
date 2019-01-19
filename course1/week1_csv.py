#Week1 - reading and writing csv
import csv
import os


os.chdir("C:/Users/TomotaY/OneDrive - BASF/Documents/Coursera/course1")

#%precision 2
# error at %

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
print(mpg[:3])

len(mpg)

#column names of csv
mpg[0].keys()
sum(float(d['cty']) for d in mpg)/len(mpg)

#set return the unique for the number of cylinders
cylinders = set(d['cyl'] for d in mpg)

#
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

vehicleclass = set(d['class'] for d in mpg) # what are the class types
vehicleclass

HwyMpgByClass = []

for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass


#string
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)

#ramda は超簡単function

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

#number comprehention
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list
#same thing
my_list = [number for number in range(0,1000) if number % 2 == 0]
my_list

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids
