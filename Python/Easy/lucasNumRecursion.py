# Write a method, lucas_number(n), that takes in a number.
# The method should return the n-th number of the Lucas Sequence.
# The 0-th number of the Lucas Sequence is 2.
# The 1-st number of the Lucas Sequence is 1
# To generate the next number of the sequence, we add up the previous two numbers.
#
# For example, the sequence begins: 2, 1, 3, 4, 7, 11, ...
#
# Solve this recursively!
#
# Examples:
#
# lucas_number(0)   # =>    2
# lucas_number(1)   # =>    1
# lucas_number(2)   # =>    3
# lucas_number(3)   # =>    4
# lucas_number(5)   # =>    11
# lucas_number(9)   # =>    76

def lucas_number(n):
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas_number(n-1) + lucas_number(n-2)

print(lucas_number(0))
print(lucas_number(1))
print(lucas_number(2))
print(lucas_number(3))
print(lucas_number(5))
print(lucas_number(9))