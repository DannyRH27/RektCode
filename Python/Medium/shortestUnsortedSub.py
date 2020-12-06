'''
Given an integer array nums, you need to find one continuous subarray that 
if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Iterate through the arr, at every num check if it is greater than the max num
'''


def findUnsortedSubarray(nums):
  curr_max = float('-inf')
  left = len(nums) - 1
  ans = 0
  for i in range(len(nums)):
    num = nums[i]
    if num >= curr_max:
      curr_max = num
    else:
      left = min(left,i-1)
      while left >= 0 and nums[left] > num:
        left -= 1
      ans = i-left
  # print(ans)
  return ans



assert(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5)
