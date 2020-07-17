def threeSum(nums, target):
  nums.sort()
  triples = []

  for i in range(len(nums) - 2):
    left = i + 1
    right = len(nums) - 1

    while left < right:
      currSum = nums[i] + nums[left] + nums[right]
      if currSum == target:
        triples.append([nums[i], nums[left], nums[right]])
        left+=1
        right-=1
      elif currSum < target:
        left+=1
      elif currSum > target:
        right-=1

  return triples
        

print(threeSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
