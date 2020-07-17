def removeDuplicates(nums):
  if not nums:
    return 0
  i, j = 1, 1

  while j < len(nums):
    if nums[j] != nums[i-1]:
      nums[i] = nums[j]
      j += 1
      i += 1
    else:
      j += 1
  return i

print(removeDuplicates([0,0,1,1,2,2,3,4,5]))
print(removeDuplicates([1, 1, 2]))

[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
