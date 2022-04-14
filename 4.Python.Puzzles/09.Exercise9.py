# https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-9.php
# Write a Python program to find list integers containing exactly four distinct values,
# such that no integer repeats twice consecutively among the first twenty entries.

def test(nums):
    return all([nums[i]!=nums[i+1] for i in range (len(nums)-1)]) and len(set(nums)) == 4

nums = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
print("Original list:",nums)
print("check the given integer list of four distinct values & no integer repeat twice conceutively :")
print(test(nums))

nums = [1,2,3,3,1,2,2,3,1,1,2,3,3,2,1,1,1,2,3]
print("\n New string is:", nums)
print("Check every conditions again.")
print(test(nums))

nums = [1,2,3,1,2,3,1,2,3,1,2,3]
print("\n\t next string:",nums)
print("I am tired of writing it over and over again So chheck it by yourself without my telling.")
print(test(nums))