'''
There is an array of n integers called num. The array can be reduced by 1 element by performing a move. 
Each move consists of the following three steps:
1. Pick two diff elements num[i] and num[j], i!=j
2. Remove the two selected elements from the array.
3. Add the sum of the two selected elements to the end of the array

Each move has a cost associated with it: the sum of the two elements removed from the arr during hte move. 
Calculate the min total cost of reducing the arr to one element.

1,2,2,2,5,7
2,2,5,7,3
5,7,3,4

heapify arr, pop pop, then add back in and heapify, then continue
'''
import heapq
def reductionCost(num):
  heapq.heapify(num)
  cost = 0
  while len(num) > 1:
    num1 = heapq.heappop(num)
    num2 = heapq.heappop(num)
    total = num1 + num2
    cost += total
    num.append(total)
    heapq.heapify(num)

  return cost


assert(arrReduction([4,6,8]) == 28)

