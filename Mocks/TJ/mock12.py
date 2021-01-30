'''
As far from land as possible

given an n x n grid square
containing values from 0 and 1
0 represents water
1 represents land

find a water cell such that the distance to the nearest land cell is maximized

return the max distance possible

0
0 1

Example 1:
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

Strategy:
okay so this sounds like dfs or bfs yayyyy

1 0 0
1 1 1
0 0 0


I will recurse and basically if it's a water cell, i'll start launching all kinds of calls until i hit a land cell
every time i move, distance will be + 1
base case is i hit land and then i will compare max of current dist and max dist and replace

if outside grid, don't launch a call

traverse grid outside and only launch if it's water
n^4


n is the length of a side
n^2
n^4


  def recurse(x, y, curr_dist, visited):
    if grid[x][y] == 1:
      visited.add((x, y))
      print(curr_dist)
      return curr_dist
    
    visited.add((x, y))
    if len(visited) == n * n:
      return -1 

    if x - 1 >= 0 and (x-1, y) not in visited:
      recurse(x-1, y, curr_dist + 1, visited)
    if x + 1 < n and (x+1, y) not in visited:
      recurse(x+1, y, curr_dist + 1, visited)
    if y - 1 >= 0 and (x, y - 1) not in visited:
      recurse(x, y-1, curr_dist + 1, visited)
    if y + 1 < n and (x, y + 1) not in visited:
      recurse(x, y+1, curr_dist + 1, visited)

1 2 3 4 5 6
2 3 4 5 6 7
1 2 3 4 5 6

O(n) check to see what my max is

FINE I WILL BFS

hint:
check dir if val

how do you keep number of steps for each one

Alternate Strategy:
outer q 

size = len(q) Keep track of levels

Get this working,
how do i do this without traversing the entire graph everytime i hit a one

if i hit a one, stored the values 
'''
from collections import deque
def maxDistance(grid):
  max_dist = -1
  n = len(grid)
  q = deque([0, 0, 0])
  visited = set()
  while q:
    x, y, dist = q.popleft()






        # max_dist = max(recurse(j, i, 0, set()), max_dist)

  return max_dist

  
    


assert(maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2)
assert(maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4)
