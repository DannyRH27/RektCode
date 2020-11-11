def twoSum(lst,n):
  print("wtf")
  if len(lst) is 0:
    return False
  lst.sort()
  left, right = 0, len(lst)-1

  while left < right:
    total = lst[left] + lst[right]
    print(lst[left],lst[right], total, n)
    if total == n:
      return [lst[left],lst[right]]
    if total > n:
      right -= 1
    if total < n:
      left += 1
  return False


# [1, 3, 5, 6, 7, 14, 21, 60]
print(twoSum([1, 21, 3, 14, 5, 60, 7, 6], 81))
