def findMaxConsecutiveOnes(nums):
  max = 0
  temp = 0
  zero_count = 0
  zero_idx = 0
  i = 0

  while i < len(nums):
    if nums[i] != 0:
      temp += 1
      i+=1
      if temp > max:
        max = temp
    
    if nums[i] == 0 and zero_count == 0:
      temp +=1
      zero_count +=1
      i+=1
      zero_idx = i
      if temp > max:
        max = temp
    elif nums[i] == 0 and zero_count != 0:
      temp = 0
      i = zero_idx
      zero_count = 0
  return max

print(findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
