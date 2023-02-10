## In real world, The data sets are much bigger, but it is really difficult to gather real world data.
## For this we are going get some help from numpy. Numpy comes with a number of methods to create rendom data
## sets of any size.

# Create an arrey containing 260 random float between 0 and 6:
import numpy
x = numpy.random.uniform(0.0, 5.0, 260)
print(x)

# To visualize the data set we can draw histogram with the data we collect.
# we will use matplotlib to draw a histogram
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 10000)

plt.hist(x,100)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()