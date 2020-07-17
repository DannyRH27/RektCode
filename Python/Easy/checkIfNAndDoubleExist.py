def checkIfExist(arr):
  s = set()
  for num in arr:
    if 2*num in s or num/2.0 in s:
      return True
    s.add(num)
  return False

print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([7, 1, 14, 11]))
print(checkIfExist([3, 1, 7, 11]))
