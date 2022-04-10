def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3

nums = [19,19,15,3,5,2,5,5,34]
print("Original list:")
print(nums)
print("check the occurance of 19 twice and atlist 3 time of 5.")
print(test(nums))

nums = [19,25,4,56,5,2,5,8,5]
print("\noriginal list:")
print(nums)
print("Again check for the nineteen for two time and five for atleast three time.")
print(test(nums))


nums = [1,2,5,5,5,19,19]
print(nums)
print(test(nums))