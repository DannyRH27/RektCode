'''
https://leetcode.com/problems/coin-change/, https://en.wikipedia.org/wiki/Change-making_problem

Umbrellas are available in different sizes that are each able to  shelter a ceterain number of people. 
Given the number of people needing shelter and a list of umbrella sizes, determine the min number of umbrellas
necessary to cover exactly the number of people given, and no more. 
If there is no combo, return -1

Strategy:
we can initiate a dictionary and mod the requirement by the umbrella sizes and use the remainders as keys
We will take the max of the umbrella sizes that lead to 0 remainders and return the requirement divided by max
if there are no perfect solutions at first, we need to mod as close as possible starting with the biggest umbrella,
then check if we have an umbrella of that size:
if not, we move on to the next biggest where we will either find an umbrella of that size or we will return -1
'''



def getUmbrellas(requirement,sizes):
  check = {}

  # for n in sizes:
  #   mod = requirement % n
  #   if mod in check:
  #     check[mod].append(n)
  #   else:
  #     check[mod] = []
  #     check[mod].append(n)
  
  # print(check)
  # if 0 in check:
  #   return requirement / max(check[0])
  
  sizes.sort(reverse = True)
  umbrellas = set(sizes)
  for umbrella in sizes:
    mod = requirement % umbrella
    count = requirement // umbrella
    
    if mod in umbrellas:
      count += 1
      break
    else:
      count = 0

  if not count:
    return -1
  return count



assert(getUmbrellas(5,[3,5]) == 1)
assert(getUmbrellas(6,[3,5]) == 2)
assert(getUmbrellas(7,[3,5]) == -1)
assert(getUmbrellas(6, [1, 3, 4]) == 2)
assert(getUmbrellas(11, [1, 3, 5]) == 3)
assert(getUmbrellas(8, [2, 3, 5]) == 3)

