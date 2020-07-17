def replaceElements(arr):
  i = len(arr) - 1
  max = arr[i]
  while i >=0:
    temp = arr[i]
    if i == len(arr)-1:
      arr[i] = -1
    else:
      arr[i] = max
    if temp > max:
      max = temp
    i-=1
  return arr

print(replaceElements([17, 18, 5, 4, 6, 1]))
