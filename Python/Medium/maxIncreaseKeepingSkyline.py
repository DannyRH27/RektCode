'''
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

'''


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid or not len(grid) or not len(grid[0]):
          return 0
        row_maxes = {}
        col_maxes = {}

        for i in range(len(grid)):
          row = grid[i]
          row_maxes[i] = max(row)

        for i in range(len(grid[0])):
          col = []
          for j in range(len(grid)):
            col.append(grid[j][i])

          col_maxes[i] = max(col)

        total_diffs = 0
        for i in range(len(grid)):
          row_max = row_maxes[i]
          for j in range(len(grid[i])):
            col_max = col_maxes[j]
            height = grid[i][j]
            max_height = min(row_max, col_max)
            total_diffs += max_height - height

        return total_diffs
