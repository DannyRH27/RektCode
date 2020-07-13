def thirdMax(nums):
  ans = set()
  for n in nums:
    ans.add(n)
    if len(ans) > 3:
      ans.remove(min(ans))

  if len(ans) == 3:
    return min(ans)

  return max(ans)
print(thirdMax([1, 1, 2]))
