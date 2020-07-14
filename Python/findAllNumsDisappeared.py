def findDisappearedNumbers(nums):
  ans = []
  for i in range(len(nums)):
    idx_check = abs(nums[i]) - 1

    if nums[idx_check] > 0:
      nums[idx_check] *= -1

  for i in range(1, len(nums)+1):
    if nums[i-1] > 0:
      ans.append(i)

  return ans  

print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
