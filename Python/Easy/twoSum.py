def twoNumberSum(array, targetSum):
    new_dict = {}
    for idx, n in enumerate(array):
      new_dict[n] = idx
    
    for n in array:
      if (targetSum - n) in new_dict and (targetSum - n) != n:
        return [n, targetSum - n]
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))
