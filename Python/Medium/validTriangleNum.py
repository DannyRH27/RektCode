def triangleNumber(nums):
  nums.sort()
  count = 0

  for i in range(len(nums)-2):
    start = i + 1
    end = start + 1
    
    while start < len(nums)-1:
      total = nums[i] + nums[start]
      while end < len(nums) and total > nums[end]:
        end+=1

      count += end-start-1
      start +=1
  # print(count)
  return count

assert(triangleNumber([2,2,3,4]) == 3)
print("Case1 Pass")
assert(triangleNumber([1,1,3,4]) == 0)
print("Case2 Pass")
assert(triangleNumber([1,2,3,4,5,6]) == 7)
print("Case3 Pass")
assert(triangleNumber([24, 3, 82, 22, 35, 84, 19]) == 10)
print("Case4 Pass")
# [3, 19, 22, 24, 35, 82, 84]
