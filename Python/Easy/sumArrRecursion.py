# Write a method, sum_array(array), that takes in an array of numbers.
# The method should return the total sum of the elements.
#
# Solve this recursively!
#
# Examples:
#
# sum_array([])             # => 0
# sum_array([5])            # => 5
# sum_array([5, 2])         # => 7
# sum_array([4, 10, -1, 2]) # => 15

def sum_array(arr):
  if not arr:
    return 0
  else:
    return arr.pop() + sum_array(arr)


print(sum_array([]))
print(sum_array([5]))
print(sum_array([5,2]))
print(sum_array([4,10,-1,2]))