def numIslands(grid):
  def dfs(i, j):
    if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == "0":
      return

    grid[i][j] = "0"
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i+1,j)
    dfs(i-1, j)

  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "0":
        continue
      count += 1
      dfs(i, j)
  print(count)
  print(grid)
  return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

assert(numIslands(grid) == 1)

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

assert(numIslands(grid2) == 3)