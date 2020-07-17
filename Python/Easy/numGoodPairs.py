def numIdenticalPairs(nums):
  count = 0
  ans = {}
  for n in nums:
    if n in ans:
      if ans[n] == 1:
        count +=1
      else:
        count += ans[n]
      
      ans[n] += 1
    else:
      ans[n] = 1

  return count
print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
