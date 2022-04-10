def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

nums = [19,19,3,2,5,5,5,9]
print("original list:")
print(nums)
print("Now check for length of the list and count of the fifth no. of the list.")
print(test(nums))

nums = [20,3,4,5,6,7,8]
print("\noriginal list:")
print(nums)
print(test(nums))