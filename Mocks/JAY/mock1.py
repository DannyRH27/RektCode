# // returns the first index where any permutation of needle begins as an exact substring of haystack, -1 if it can't find it
# // permutation("abc") = > "abc", "acb", "bac", "bca", "cab", "cba"
# // strstrp("hello there", "hello") returns 0
# // strstrp("hello there", "elloh") returns 0
# // strstrp("hello there", "o there") returns 4
# // strstrp("hello there", "the reo") returns 4
# // strstrp("hello there", "jefwoai") returns - 1
# // strstrp("aa", "a") returns 0
# int strstrp(string haystack, string needle)


# first i need to get the permutations of the needle
# for every perm, i'll just check if it is in the string
# if it it's not then i'll return -1
# if it is, then i know which permutation it is.
# then i just call python strstr method is and return that index

# implement arePermutations(str1,str2) 


# currently slice through the haystack with two pointers O(h)

# see what the differences are, then move by the number of differences.

from collections import Counter

def strstrp(haystack,needle):

  point1 = 0
  point2 = len(needle)
  count = Counter(needle)
  word = haystack[point1:point2]
  for char in word:
    count[char] -= 1
    if count[char] == 0:
      del count[char]

  if len(count) == 0:
    return point1
  while point2 < len(haystack):
    deleted = haystack[point1]
    added = haystack[point2]

    count[deleted] += 1
    if count[deleted] == 0:
      del count[deleted]

    count[added] -= 1
    if count[added] == 0:
      del count[added]
    # print(count,point1, point2, diffs)

    point1 += 1
    point2 += 1
    if len(count) == 0:
      return point1


  return -1


# assert(strstrp("hello there", "hello") == 0)
# assert(strstrp("hello there", "h") == 0)
# assert(strstrp("hello there", "e") == 1)
# assert(strstrp("hello there", "l") == 2)
# assert(strstrp("hello there", "elh") == 0)
# assert(strstrp("hello there", "olleh") == 0)
# assert(strstrp("hello there", "elloh") == 0)
# assert(strstrp("hello there", "helol") == 0)
# assert(strstrp("hello there", "ehllo") == 0)
print(strstrp("ellho there", "oth "))
#assert(strstrp("hello there", "oth ") == 4)
#assert(strstrp("hello there", "o th") == 4)
assert(strstrp("ellho there", "oth ") == 3)
assert(strstrp("hello there", "there") == 6)
assert(strstrp("hello there", "eethr") == 6)
assert(strstrp("hello there", "three") == 6)
assert(strstrp("hello there", "ere") == 8)
assert(strstrp("hello there", "fwoaifj") == -1)
assert(strstrp("hello", "hello there") == -1)
assert(strstrp("hehea waw", "hea") == 2)
assert(strstrp("hehea waw", "eha") == 2)
assert(strstrp("hehea waw", "ahe") == 2)
assert(strstrp("heehea", "heea") == 2)
assert(strstrp("hello there", "lot") == -1)
assert(strstrp("heoll llale", "ell") == -1)
assert(strstrp("heoll llale", "eol ") == -1)
assert(strstrp("heoll llale", " eol") == -1)
assert(strstrp("aabe", " aaabe") == -1)
assert(strstrp("", "a") == -1)
assert(strstrp("", "b") == -1)
assert(strstrp("", " ") == -1)
print("All test cases passed!")
