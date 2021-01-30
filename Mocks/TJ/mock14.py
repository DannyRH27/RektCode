'''
last stone weight II
recursively smash all

knapsack problem
separate two groups that have the lowest difference

PRACTICE DP/Knapsack

wtf does |=

def lastStoneWeightII(self, A):
    dp = {0}
    sumA = sum(A)
    for a in A:
        dp |= {a + i for i in dp}
    return min(abs(sumA - i - i) for i in dp)
'''


def lastStoneWeightII(stones):
  min_stone = float('inf')
  smashed = set()

  return min_stone


assert(lastStoneWeightII([31, 26, 33, 21, 40]) == 5)
