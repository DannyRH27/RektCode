class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#       sort array,
#       loop through and if first pointer is a duplicate, continue
#       target is negative i
#       left, right is second and last
#       while left < right:
#       sum is left + right
#       if sum is < target, increase left, decrease right, then add arr
#       check for duplicates on both sides
      nums.sort()
      triplets = set()
      
      for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
          continue
        start = i+1
        end = len(nums)-1
        target = -nums[i]
        while start < end:
          sum = nums[start] + nums[end]
          
          if sum == target:
            triplets.add((nums[start], nums[i], nums[end]))
            while start < end and nums[start] == nums[start+1]:
              start += 1
            start += 1
            
            while start < end and nums[end] == nums[end-1]:
              end -=1
            end -= 1
            
          elif sum < target:
            start += 1
          else:
            end -= 1
            
      return triplets