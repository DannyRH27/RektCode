def heightChecker(heights):
  sorted_heights = sorted(heights)

  i = 0
  count = 0
  while i < len(heights):
    if heights[i] != sorted_heights[i]:
      count+=1
    i+=1

  return count


print(heightChecker([1, 1, 4, 2, 1, 3]))
