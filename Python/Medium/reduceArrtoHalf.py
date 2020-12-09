
from collections import Counter
def minSetSize(arr):
  count = Counter(arr)

  items = list(count.items())
  items.sort(reverse=True,key = lambda x: x[1])

  n = len(arr)
  num_count = 0
  count = 0
  print(items)
  for item in items:
    if num_count < (n/2):
      num_count += item[1]
      count += 1
      print(num_count,count,item)
  return count

assert(minSetSize([3,3,3,3,5,5,5,2,2,7]) == 2)
assert(minSetSize([5, 5, 5, 3, 3, 3, 3, 2, 2, 7]) == 2)
