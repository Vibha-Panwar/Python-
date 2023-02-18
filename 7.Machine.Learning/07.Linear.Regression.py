## Regression :--> The meaning of regression is to find relationship between variable.
## In machine learning, That relationship is used to predict the outcome of future events.
## The linear regression uses the relationship between the points to draw a straight through all of them.
## This line can be used to predict the future values.

import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
    return slope*x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()