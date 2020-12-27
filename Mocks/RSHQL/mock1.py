'''
Company interviews 2N people

given arr costs where costs[i]
[aCosti, bCosti]

cost of flying person to city A is aCosti
cost of flying ith person to city B is bCosti

return min cost to fly every person to a city such that N people arrive at each city

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
A, A, B, B
Output: 110

[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

List of abs diff between each choice and sort


259 54 667 184 118 577
A B B A B A
1859

259 => 770

448 => 54


A heap and a B heap

min heapify

do min of both and compare to each other and then check choices



then I'll make my choices greedily


len(costs) tells me how many people i have to fly

DP Approach:
I could recurse and always make a different choice at each point and at the end i'll add it to a list
then I can do an O(N) min operation to find the lowest cost

recurse strat:
Base case is going to be when i is equal to the len(arr), i will add the total to my DP table
Need to feed it a choice, total, and i

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000

tup, (abs, choice)
'''

def twoCitySchedCost(costs):

  check = []

  for cost in costs:
    if cost[0] < cost[1]:
      check.append((abs(cost[0]-cost[1]),'a'))
    else:
      check.append((abs(cost[0]-cost[1]),'b'))
  
  for i in range(len(costs)):
    diff = check[i][0]
    costs[i].append(diff)

  check.sort(reverse=True)
  costs.sort(reverse=True,key = lambda x: x[2])

  a = 0
  b = 0

  n = len(costs) / 2
  total = 0
  for cost in costs:
    choice_A = cost[0]
    choice_B = cost[1]

    if choice_A < choice_B:
      if a < n:
        total += choice_A
        a += 1
      else:
        total += choice_B
        b += 1
    else:
      if b < n:
        total += choice_B
        b += 1
      else:
        total += choice_A
        a += 1

  return total

      
    
# assert(twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110)
assert(twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859)
