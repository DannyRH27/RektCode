def shiftedBinarySearch(array, target):

  left = 0
  right = len(array) - 1

  while left <= right:
      pivot = (left + right) // 2
      potentialMatch = array[pivot]
      if potentialMatch == target:
        return pivot
      elif potentialMatch >= array[left]:
        if target < potentialMatch and target >= array[left]:
          right = pivot - 1
        else:
          left = pivot + 1
      else:
        if target > potentialMatch and target <= array[right]:
          left = pivot + 1
        else:
          right = pivot - 1
  return -1
