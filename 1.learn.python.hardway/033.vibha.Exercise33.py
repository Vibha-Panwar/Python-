# In this exercise I will use while function and append() function.
# while function is  little bit tough for me. still going to try it.

i = 1990
Years = []

while i < 1998:
    print(f"At the  top i is {i}")
    Years.append(i)
    i += 1
    print(f"Year Now:",Years)
    print(f"At the bottom i is {i}")

print("The Years are:")

for Year in Years:
    print(Year)