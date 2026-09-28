# Find the Minimum Element in an Array

min_count = nums[0]

for num in nums:
    if num < min_count:
        min_count = num

return min_count
