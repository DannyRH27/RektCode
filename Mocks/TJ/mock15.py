'''
given an n by n matrix of int called matrix
return the min sum of any falling path 

falling path starts at any elements and chooses any ele directly below or diagonally left or right

1   4  3
2   2  1
-20 4  1

could also have negative numbers

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],
 [6,5,4],      
 [7,8,9]]       

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is underlined below:
[[-19,57],
 [-40,-5]]

Example 3:
Input: matrix = [[-48]]
Output: -48


Brute Force:
iteraviely loop through the first row and launch recursive calls to go through everything
O(n) min call at the end to get the min out of the arr that stores the sums
Runtime: O(X^2) O(N^4) could be exponential
Memory: O(V+E) for recursive stack space and O(N) for the array to store my existing sums

DP:
I Suck, not doing this
'''
# [[1,4,7,2],
#  [5,2,2,6]
#  [7,-2,-5,3]
#  [-50,8,8,8]]

# tabulation
# ive got first row
# start on row 2
# go backwards

def minFallingPathSum(matrix):    
  ans = matrix[0]

  row = 1
  while row < len(matrix):
    temp_row = ans.copy()
    for i, num in enumerate(matrix[row]):
      choices = []
      if i - 1 >= 0:
        choices.append(num + ans[i-1])
      choices.append(num + ans[i])
      if i + 1 < len(matrix):
        choices.append(num + ans[i+1])
      temp_row[i] = min(choices)
    ans = temp_row.copy()
    row += 1

  return min(ans)


assert(minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13)
assert(minFallingPathSum([[-19, 57], [-40, -5]]) == -59)
assert(minFallingPathSum([[-48]]) == -48)

# def minFallingPathSum(matrix):
#   abs_min = float('inf')

#   def recurse(x, y, curr_min):
#     nonlocal abs_min
#     if y > len(matrix) - 1:
#       abs_min = min(curr_min, abs_min)
#       return


#     curr_min += matrix[y][x]
#   # launch a call directly down
#     recurse(x, y+1, curr_min)

#   # launch a call diagonally left
#     if x - 1 >= 0:
#       recurse(x-1, y+1, curr_min)

#   # launch a call diagonally right
#     if x + 1 < len(matrix):
#       recurse(x+1, y+1, curr_min)

    
#   for x in range(len(matrix[0])):
#     recurse(x, 0, 0)
#   return abs_min



