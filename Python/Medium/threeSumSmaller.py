def threeSumSmaller(nums, target):
    nums.sort()
    count = 0

    for i in range(len(nums)-2):


      # if i > 0 and nums[i] == nums[i-1]:
      #   continue

      start = i + 1
      end = len(nums) - 1

      while start < end:
        total = nums[i] + nums[start] + nums[end]

        if total < target:
          count += end - start
          start += 1
        else:
          end -=1
    return count

assert(threeSumSmaller([-2,0,1,3], 2) == 2)
assert(threeSumSmaller([1,1,-2], 1) == 1)
assert(threeSumSmaller([3,1,0,-2], 4) == 3)
assert(threeSumSmaller([-1,1,-1,-1], -1) == 1)
# [-1,-1,-1,1]
