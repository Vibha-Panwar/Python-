## When I read this in tutorials, I didn't get anything what is it trying to say.
# So let me tell you about it in the same way with which i get to understand it.
# Percentiles -- let say we have an arrey of ages. In this arrey we have 10 entry and if we want 70 percentile
# of this arrey then program will give us a number. we will know that 70% of people age of the arrey is equal or 
# younger then that number. We will understand it more after the proper example.
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,26,36,27,61,31] # we give this arrey
x = numpy.percentile(ages,75) # here we want 75 percentile of ages arrey with the help of numpy.
print(x)
# we got the answer 43.0 that means 75% of ages are either 43 or younger then 43.
