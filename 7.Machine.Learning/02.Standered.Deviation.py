# Standard Deviation:--> It is a number that describes how spread out the values are.
# A low Standard Deviation means- no. are close tp mean value.
# A High Standard Deviation means- no. are spread out over a wider range.
import numpy
speed = [86,87,88,86,85,86,87]
x = numpy.std(speed)
print(x)

# Variance: it is another number that indicates how spread out the values are.
# How to calculate it :-->
# 1] Find the mean
# 2] Find the difference from the mean for each value
# 3] Do square value of the difference we took in step 2.
# 4] Now find mean of the square value. you will get the Vaiance.

# Standered Deviation :--> Square root of Variance
