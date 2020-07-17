def sortedSquares(A):
  i = 0
  j= len(A)-1
  ans = [0] * len(A)
  print(ans)
  while i <= j:
    if abs(A[i]) ** 2 > abs(A[j]) ** 2:
      ans[j-i] = abs(A[i]) ** 2
      i+=1
    else:
      ans[j-i] = abs(A[j]) ** 2
      j-=1
  return ans

print(sortedSquares([-7, -3, 2, 3, 11]))
