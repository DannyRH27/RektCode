from functools import lru_cache

def isMatch(str1,str2):
  @lru_cache(10000)
  def recurse(slice1, slice2):
    if len(slice1) == 0 and len(slice2) == 0:
      return True

    if len(slice2) == 0:
      return False
      
    if len(slice1) == 0:
      for c in slice2:
        if c != "*":
          return False
      return True

    if slice1[0] == slice2[0] or slice2[0] == "?":
      return recurse(slice1[1:], slice2[1:])

    if slice2[0] == "*":

      return recurse(slice1, slice2[1:]) or recurse(slice1[1:], slice2)

    else:
      return False
    
  return recurse(str1,str2)

isMatch("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "**************************a")