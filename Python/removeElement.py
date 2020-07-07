def removeElement(nums, val):
    i = 0
    j = 0

    while j < len(nums):
      if nums[j] != val:
        nums[i] = nums[j]
        j += 1
        i += 1
      else:
        j += 1
    return i


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
