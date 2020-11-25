def threeSum(nums):
  nums.sort()
  res = []
  for i in range(len(nums)):
    if nums[i] > 0:
      break
    if i == 0 or nums[i] != nums[i-1]:
      j = i + 1
      seen = set()
      while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
          res.append([nums[i],nums[j], complement])
          while j+1 < len(nums) and nums[j] == nums[j+1]:
            j+=1
        seen.add(nums[j])
        
        j+= 1
  return res
          
print(threeSum([-1, 0, 1, 2, -1, -4]))
# [-4, -1, -1, 0, 1, 2]