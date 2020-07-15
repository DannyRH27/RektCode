def runningSum(nums):

  sum = 0
  i = 0

  while i < len(nums):
    sum += nums[i]
    nums[i] = sum
    i +=1

  return nums

