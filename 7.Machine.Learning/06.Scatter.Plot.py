 # Scatter Plot  :-- It is a where each value in the data set is represent by a dot. It needs 2 array of same length.
 # One for x axis and second one for y-axis.
import sys
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()