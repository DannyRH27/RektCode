def findThreeLargestNumbers(array):
    # Write your code here.
  new_arr = [None] * 3


  for n in array:
    if new_arr[-1] == None or n > new_arr[-1]:
      new_arr[-3] = new_arr[-2]
      new_arr[-2] = new_arr[-1]
      new_arr[-1] = n
    elif new_arr[-2] == None or n > new_arr[-2]:
      new_arr[-3] = new_arr[-2]
      new_arr[-2] = n
    elif new_arr[-3] == None or n > new_arr[-3]:
      new_arr[-3] = n

  return new_arr
