'''
Some digits are formed with closed paths. The digits 0,4,6 and 9 each have 1 closed path, and 8 has 2. 
None of the other numbers is formed with a closed path. 
Given a number, determine the total number of closed paths in all of its digits combined.

number = 649578
The digits with closed paths are 6,4,9 and 8. The total number of closed paths is 1 + 1 + 1 + 2 = 5
'''


def closedPaths(number):
  str_num = str(number)
  closed = set([0,4,6,9])
  closed_paths = 0
  for str_digit in str_num:
    digit = int(str_digit)
    if digit in closed:
      closed_paths += 1
    
    if digit == 8:
      closed_paths += 2

  return closed_paths

assert(closedPaths(649578) == 5)
assert(closedPaths(1288) == 4)
assert(closedPaths(630) == 2)
