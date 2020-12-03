def rotate(nums,k):
  count = k % len(nums)
  nums = nums[k+1:] + nums[:k+1]
  print(nums, count)
assert(rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4])
