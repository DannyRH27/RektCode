import math
def findMin(nums):
  if len(nums) == 1 or nums[0] < nums[-1]:
    return nums[0]

  # left = 0
  # right = len(nums) - 1

  # while left < right:
  #   mid = int(math.floor((left / 2) + (right / 2)))
  #   prev = mid - 1
  #   nextt = mid + 1

  #   if prev >= 0:
  #     if nums[prev] > nums[mid]:
  #       return nums[mid]

  #   if nextt < len(nums):
  #     if nums[nextt] < nums[mid]:
  #       return nums[nextt]

  #   if nums[mid] > nums[right]:
  #     left = mid + 1
  #   else:
  #     right = mid - 1

  # def bsearch(left,right):

  #   if left > right:
  #     return

  #   mid = int(math.floor((left / 2) + (right / 2)))

  #   prev = mid - 1
  #   nextt = mid + 1
  #   if prev >= 0:
  #     if nums[prev] > nums[mid]:
  #       return nums[mid]

  #   if nextt < len(nums):
  #     if nums[nextt] < nums[mid]:
  #       print(nextt,nums[nextt])
  #       return nums[nextt]

  #   if nums[mid] < nums[right]:
  #     bsearch(left,mid-1)
  #   else:
  #     bsearch(mid+1,right) 

  # return bsearch(0, len(nums)-1)


# assert(findMin([3, 4, 5, 1, 2]) == 1)
# assert(findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
assert(findMin([2, 3, 4, 5, 1]) == 1)
assert(findMin([5, 1, 2, 3, 4]) == 1)
