def findNumbers(nums):
  count = 0
  for n in nums:
    if len(list(str(n))) % 2 == 0:
      count +=1
  return count

print (findNumbers([555, 901, 482, 1771]))
