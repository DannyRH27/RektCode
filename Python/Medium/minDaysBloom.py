'''
Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

binary search to find day
lower bound is min(bloom)
upper bound is max(bloom)

at every step, need to check if it is possible to make bouqets
go through arr, create new arr that has flowers bloomed.
Return True if we can make bouqets

'''
import math
def minDays(bloomDay, m, k):
  if m * k > len(bloomDay):
    return -1
  def possible(days):
    garden = ["x" if n <= days else "_" for n in bloomDay]

    bouqets = 0
    count = 0
    for i in range(len(garden)):
      if garden[i] == "x":
        count += 1
        if count == k:
          bouqets += 1
          count = 0
      else:
        count = 0

    if bouqets >= m:
      return True
    return False
  possible(3)

  def bsearch(left, right):
    avg = math.floor((left / 2) + (right / 2))
    while left < right:
      if possible(avg):
        return bsearch(left, avg)
      else:
        return bsearch(avg+1,right)

    return avg

  return bsearch(min(bloomDay),max(bloomDay))

assert(minDays([1, 10, 3, 10, 2],3,1) == 3)
assert(minDays([1, 10, 3, 10, 2],3,2) == -1)
assert(minDays([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12)
