def validMountainArray(A):
  if len(A) <= 2:
    return False
  count = 0
  i = 1
  if A[0] > A[1]:
    return False
  while i < len(A):
    if A[i-1] == A[i]:
      return False

    if A[i-1] > A[i] and count == 0:
      count += 1
    
    if A[i-1] < A[i] and count == 1:
      return False
    i+=1
  if count == 1:
      return True


print(validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
