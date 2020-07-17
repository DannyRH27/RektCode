def containsDuplicate(nums):
  ans = set(nums)

  if len(ans)< len(nums):
    return True
  return False