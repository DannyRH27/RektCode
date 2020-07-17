def smallerNumbersThanCurrent(nums):
  sorted_nums = sorted(nums)
  new_dict = {sorted_nums[0]:0}
  i=1

  while i < len(nums):
    print(new_dict)
    print (sorted_nums)
    print (sorted_nums[i])
    print('----')
    print (sorted_nums[i-1])
    print('----')
    print (i)
    print('next iteration')
    if sorted_nums[i] > sorted_nums[i-1]:
      new_dict[sorted_nums[i]] = i
    i+=1

  return [new_dict[i] for i in nums]


  

print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
# print(smallerNumbersThanCurrent([6, 5, 4, 8]))
# print(smallerNumbersThanCurrent([7, 7, 7, 7]))
