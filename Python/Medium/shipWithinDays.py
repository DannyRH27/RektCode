'''
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
'''

'''
minimum bound:
ship needs to be at least able to carry only the max package.

max bound:
ship needs to carry everything

binary search

fill to capacity and then decrement day_count
if day_count is 0, increase bag capacity by one

''' 
import math
def shipWithinDays(weights, D):

  def possible(capacity):

    count = 0
    total = 0
    for weight in weights:
      if total + weight > capacity:
        total = 0
        count += 1
        
      total += weight

    if count >= D and total > 0:
      return False
    return True
    
  def bsearch(left,right):

    avg = int(math.floor((left / 2) + (right / 2)))

    while left < right:
      if possible(avg):
        return bsearch(left, avg)
      else:
        return bsearch(avg+1, right)
    return avg

  return bsearch(max(weights),sum(weights))
  


assert(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5) == 15)


  
