'''
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
'''

def canPlaceFlowers(flowerbed,n):
  if n == 0:
    return True
  if len(flowerbed) == 0:
    return None

  if len(flowerbed) == 1:
    if flowerbed[0]:
      return n == 0
    else:
      return n == 1

  count = 0
  for i in range(len(flowerbed)):
    if i == 0:
      if flowerbed[i] == 0:
        if flowerbed[i+1] == 0:
          flowerbed[i] = 1
          count += 1
    elif i == len(flowerbed)-1:
      if flowerbed[i] == 0:
        if flowerbed[i-1] == 0:
          count += 1
    else:
      if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        flowerbed[i] = 1
        count += 1


  return count >= n



# assert(canPlaceFlowers([1, 0, 0, 0, 1],1)== True)
# assert(canPlaceFlowers([1, 0, 0, 0, 1],2)== False)
# assert(canPlaceFlowers([0],1) == True)
# assert(canPlaceFlowers([1],1) == False)
# assert(canPlaceFlowers([1],0) == True)
# assert(canPlaceFlowers([0, 0, 1, 0, 0], 1) == True)
# assert(canPlaceFlowers([0, 0, 0, 0, 1], 2) == True)
# assert(canPlaceFlowers([1, 0, 0, 0, 1], 2) == False)
assert(canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 1) == False)
