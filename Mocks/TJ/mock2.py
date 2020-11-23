'''
find contiguous subarr that has at least one number which has the largest sum,
return the sum

this is a sliding window problem,
use one pointer and abs_max, curr_max
if the next num makes curr_max less than 0, we can reset curr_max to 0 and move the pointer to the num after, then continue
if the next num is bigger than curr_max and negative, then also start over
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Constraints:
1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1

Example 4:
Input: nums = [-1]
Output: -1

[-1,-2,-3]

'''


def maxSubArray(nums):
  abs_max = nums[0]

  pointer = 0

  curr_sum = 0
  while pointer < len(nums):
    if curr_sum < 0:
      curr_sum = 0

    curr_sum += nums[pointer]

    if curr_sum > abs_max:
      abs_max = curr_sum

    pointer += 1

  return abs_max
