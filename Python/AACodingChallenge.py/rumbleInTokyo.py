def minBlows(height):

  def helper(arr, moves):
    if len(arr) == 1:
      return moves + 1

    if len(arr) == 0:
      return moves

    count = 1
    count2 = 1

    point1 = 0
    point2 = len(arr)-1
    while point1 + 1 < len(arr) and arr[point1] <= arr[point1+1]:
      point1 += 1
      count += 1
    while point2 - 1 >= 0 and arr[point2] <= arr[point2-1]:
      point2 -= 1
      count2 += 1
    if count >= count2:
      arr = arr[count:]
    else:
      arr = arr[:len(arr)-count2]

    return helper(arr, moves+1)

  return helper(height, 0)



assert(minBlows([1,2,3,4,3,2,3,2,1]) == 3)
assert(minBlows([1,2,3,2,3,2,4,3,2,1]) == 4)
assert(minBlows([1,2,1,2,7,8,2,1,2,1]) == 4)
assert(minBlows([2,2,2,2,2,2,2]) == 1)
