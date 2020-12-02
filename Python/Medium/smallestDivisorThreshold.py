import math
def smallestDivisor(nums, threshold):
  def possible(divisor):
    new_nums = [math.ceil(n/divisor) for n in nums]
    total = sum(new_nums)
    if total <= threshold:
      return True
    return False


  def bsearch(left, right):
    avg = math.floor((left/2) + (right/2))
    while left < right:
      if possible(avg):
        return bsearch(left,avg)
      else:
        return bsearch(avg+1,right)

    return avg
  return bsearch(1,max(nums))

# assert(smallestDivisor([1, 2, 5, 9],6)==5)
# assert(smallestDivisor([2, 3, 5, 7, 11], 11) == 3)
assert(smallestDivisor([19], 5) == 4)
