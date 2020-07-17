def decompressRLElist(nums):
  ans = []
  i = 0

  while i < len(nums):
    new_arr = [nums[i+1]] * nums[i]
    ans += new_arr
    i+=2

  return ans

print(decompressRLElist([1,2,3,4]))
print(decompressRLElist([1,1,2,3]))