def createTargetArray(nums, index):

  res = []

  for i, n in zip(index, nums):
    res = res[:i] + n + res[i:]
  return res