def fourSum(nums, target):
  res = []
  nums.sort()
  my_dict = {}
  # print(nums)
  for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
      key = nums[i] + nums[j]
      if key in my_dict:
        if (i,j) not in my_dict[key] and (j,i) not in my_dict[key]:
          my_dict[key].add((i,j))
      else:
        my_dict[key] = set()
        my_dict[key].add((i,j))
  tup_set = set()
  for i in range(len(nums)-1):

    for j in range(i+1, len(nums)):

      complement = target - (nums[i] + nums[j])
      if complement in my_dict:
        for tup in my_dict[complement]:
          if tup[0] != i and tup[1] != i and tup[0] != j and tup[1] != j:
            check = [nums[tup[0]], nums[tup[1]], nums[i], nums[j]]
            check.sort()
            new_tup = tuple(check)
            if new_tup in tup_set:
              continue
            tup_set.add(new_tup)
            res.append(check)
  return res

assert(fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
# [-2, -1, 0, 0, 1, 2]
