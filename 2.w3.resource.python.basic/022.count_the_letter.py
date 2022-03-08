# https://www.w3resource.com/python-exercises/python-basic-exercise-22.php

# Write a Python program to count the number 4 in a given list

def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
        
    return count

print(list_count_4([1,4,7,9,4,2]))
print(list_count_4([2,3,4,5,8,4,4,5,4]))