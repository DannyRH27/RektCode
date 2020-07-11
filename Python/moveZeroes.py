def moveZeroes(nums):
  zero_count = nums.count(0)
  i = 0
  j = 0

  while i < len(nums) - zero_count:
    if nums[j] != 0:
      nums[i] = nums[j]
      i+=1
      j+=1
    else:
      j+=1
  
  while i < len(nums):
    nums[i] = 0
    i+=1
  return nums

  

print(moveZeroes([0, 1, 0, 3, 12]))
