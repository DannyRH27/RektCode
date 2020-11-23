'''
Given an integer array nums, 
find the contiguous subarray within an array (containing at least one number) which has the largest product.
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
'''
abs max and current max initialize as first
pointer to iterate through
check if curr_max times pointer = 0, if it does, then reset curr_max to 0
every number, check if curr_max times pointer number is greater than abs max, if so replace abs max
'''
def maxProduct(nums):
  if len(nums) == 1:
    return nums[0]

  abs_max = nums[0]
  curr_max = abs_max 
  curr_min = abs_max
  pointer = 1
  while pointer < len(nums):
    temp_max = max(curr_max * nums[pointer], nums[pointer], curr_min * nums[pointer])
    curr_min = min(curr_max * nums[pointer], nums[pointer], curr_min * nums[pointer])
    
    curr_max = temp_max
    if curr_max > abs_max:
      abs_max = curr_max
    pointer += 1

  return abs_max

assert(maxProduct([2,3,-2,4]) == 6)
assert(maxProduct([-2,0,-1]) == 0)
assert(maxProduct([2, -5, -2, -4, 3]) == 24)
assert(maxProduct([3, -1, 4]) == 4)
assert(maxProduct([-2, 3, -4]) == 24)
assert(maxProduct([0, 2]) == 2)
