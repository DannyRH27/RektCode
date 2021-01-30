'''
Collection of stones
Each stone has a positive int weight
Each turn, choose the two heaviest stones and smash together
x, y
x <= y
if they are the same, both stones destroyed
if not, stone with lesser weight is destroyed, stone with bigger weight is difference

At the end, there is at most one stone left. Return weight of this stone or 0 if no stones are left.

Strategy:
In order to know which stones are always the heaviest
I will have a max heap of these stones
while the length of this heap is >= to 2
I will heappop one, heappop again,
if they are the same, both stones are destroyed
if they are different, then i will heappush that difference onto the heap

eventually when the heap is 1 or 0, depending on which i will return the stone or 0

Get the smallest possible last rock or return 0 if there are none
What is the heuristic for determining which rocks to pick

Brainstorm:
I always want to be nullifying the biggest number
Can't tell by looking at the stones
what do i want the result of smashing the stones together to be

Outcome is the smallest rock


Brute Force:
Launch calls to smash them all
push answers to a min_heap
then return the min

runtime: nlogn
space: n

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''

import heapq
def lastStoneWeight(stones):
  heapq._heapify_max(stones)
  
  while len(stones) >= 2:
    first = heapq._heappop_max(stones)
    second = heapq._heappop_max(stones)

    if first == second:
      continue

    heapq.heappush(stones, first-second)
    heapq._heapify_max(stones)

  if len(stones):
    return stones[0]

  return 0


# assert(lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1)
# assert(lastStoneWeight([10, 4, 2, 10]) == 2)
assert(lastStoneWeight([7, 6, 7, 6, 9]) == 3)
