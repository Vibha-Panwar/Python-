# https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-7.php
# Write a Python program to check a given list of integers where the sum of the first i integers is i.

def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])

nums1 = [0,1,2,3,4,5]
print("original list:")
print(nums1)
print("check the said list,the Sum of the first i integers is i.")
print(test(nums1))

nums2 = [1,1,1,1,1,1,1,1]
print("\nnew list:",nums2)
print("Check the condition again.")
print(test(nums2))