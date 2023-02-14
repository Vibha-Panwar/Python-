## In last tutorial, we learn to create completely random arrey, of given size, and between two values.
## In this tutorial, we learn to create an arrey where the values are concentrated around a given value.

import sys
import matplotlib
matplotlib.use("Agg")

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x,1000)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

## Explanation :--> we use arrey numpy.random.normal() with values 100000, to draw a histogram with 1000 bars.
## here we specify - mean value = 5.0 and standard value  = 1.0
## means values should be concentrated around 5.0 and rarely further away then 1.0 from the mean. 