# Mean = The average Value
# Median = The mid point value
# Mode = The most common value

# Mean :--
import numpy
speed = [99,86,88,87,86,103,111,87,94,77,78,85,86]
x = numpy.mean(speed)
print(x)

# Median :--
import numpy
speed = [12,13,14,15,16,17,18]
x = numpy.median(speed)
print(x)

# If there is even numbers in the list then sum the middle two number and divide by 2. This will be your median no.
import numpy
speed = [1,2,3,4,5,6]
x = numpy.median(speed)
print(x)
'''
# Mode :--
from scipy import stats
speed = [1,2,3,1,3,1,1,1,3]
x = stats.mode(speed)
print(x)
'''