def findClosestElements(arr, k, x):
  left = 0
  right = len(arr) - 1
  index = False
  
  while left <= right:
    pivot = (left + right) // 2
    potentialMatch = arr[pivot]

    if potentialMatch == x:
      index = pivot
    elif potentialMatch > x:
      left = pivot + 1
    else:
      right = pivot - 1
  

  print(findClosestElements)
  



print(findClosestElements([1,2,3,4,5],4,3))
print(findClosestElements([1,2,3,4,5],4,-1))
