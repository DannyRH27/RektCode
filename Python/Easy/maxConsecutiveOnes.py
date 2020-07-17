def findMaxConsecutiveOnes(nums):
  max = 0
  temp = 0
  for n in nums:
      if n == 1:
          temp += 1
          if temp > max:
              max = temp
      else:
          temp = 0
  return max


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
