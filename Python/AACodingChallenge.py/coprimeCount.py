'''
Two integers are said to be co-primes if their greatest common divisor is 1. 
Given an array of positive integers, A, return an array of integers B, 
where B[i] = count of integers j such that  1 <=j<=A[i] and j is co-prime with respected to A[i].

A = [5,8,14]

The number A[0] = 5 is prime. All numbers greater than 0 and less than 5, i.e. 1-4 are co-prime with 5 so B[0] = 4
For A[1] = 8, the integers [2,4,6] share at least the common divisor of 2 with 8. 
The 4 values, [1,3,5,7], are co-primes, so B[1] = 4.
For A[2] = 14, the integers [2,4,6,7,8,10,12] share a common divisor > 1 with 14. 
The 6 co-primes are [1,3,5,9,11,13], so B[2] = 6.
The return arr is B = [4,4,6]
'''

def coprimeCount(A):

  def isCoprime(x, y):
    while y != 0:
      x, y = y, x % y
    return x

  B = [0] * len(A)
  for i in range(len(A)):
    count = 0
    for j in range(1,A[i]):
      if isCoprime(j,A[i]) == 1:
        count += 1
    B[i] = count

  return B


assert(coprimeCount([5,8,14]) == [4,4,6])



  
