def duplicateZeroes(arr):
  zeroes = arr.count(0)
  n = len(arr)
  for i in range(n-1, -1, -1):
    if i + zeroes < n:
      arr[i + zeroes] = arr[i]
    if arr[i] == 0:
      zeroes -= 1
      if i + zeroes < n:
        arr[i + zeroes] = 0
  print (arr)

duplicateZeroes([1, 0, 2, 3, 0, 4, 5, 0])
duplicateZeroes([1, 2, 3])
duplicateZeroes([1,2,3,0,0,0])
duplicateZeroes([1,2,3,0,0,5])