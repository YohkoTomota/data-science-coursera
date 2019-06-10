import matplotlib as mpl

mpl.get_backend()
import matplotlib.pyplot as plt

plt.plot(3, 2)
plt.plot(3, 2, '.')
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

##################basic

# create a new figure
fig = Figure()

# associate fig with the backend
canvas = FigureCanvasAgg(fig)

# add a subplot to the fig
ax = fig.add_subplot(111)

# plot the point (3,2)
ax.plot(3, 2, '.')

# create a new figure
plt.figure()

# plot the point (3,2) using the circle marker
plt.plot(3, 2, 'o')

# get the current axes
ax = plt.gca()

# Set axis properties [xmin, xmax, ymin, ymax]
ax.axis([0,6,0,10])

# create a new figure
plt.figure()

# plot the point (1.5, 1.5) using the circle marker
plt.plot(1.5, 1.5, 'o')
# plot the point (2, 2) using the circle marker
plt.plot(2, 2, 'o')
# plot the point (2.5, 2.5) using the circle marker
plt.plot(2.5, 2.5, 'o')


############scatter plot

import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

# create a list of colors for each point to have
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red']
colors = ['green']*(len(x)-1)
colors.append('red')

plt.figure()

# plot the point with size 100 and chosen colors
plt.scatter(x, y, s=100, c=colors)

############Bar charts

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

plt.figure()
# plot the linear data and the exponential data
plt.plot(linear_data, '-o', exponential_data, '-o')

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)

new_xvals = []

# plot another set of bars, adjusting the new xvals to make up for the first set of bars plotted
for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals, exponential_data, width = 0.3 ,color='red')

from random import randint
linear_err = [randint(0,15) for x in range(len(linear_data))] 

# This will plot a new set of bars with errorbars using the list of random error values
plt.bar(xvals, linear_data, width = 0.3, yerr=linear_err)

# stacked bar charts are also possible
plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, exponential_data, width = 0.5, bottom=linear_data, color='r')

# or use barh for horizontal bar charts
plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color='b')
plt.barh(xvals, exponential_data, height = 0.3, left=linear_data, color='r')


########multiple stack bar
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(index=['06-11-2018', '06-12-2018', '06-13-2018',
                         '06-14-2018', '06-15-2018'], 
                  data={'A': [-378, 2347, 509, 987, 513], 
                        'B': [527, 2599, -765, 533, 670], 
                        'C': [2343, -2273, 2093, -2197, 1990], 
                        'D': [1845, 1853, -3325, 1306, 2160]})

ax = df.plot(kind="bar", stacked=True)
df.sum(axis=1).plot(ax=ax, color="k")

plt.show()