'''
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

traverse through the binary tree through DFS or BFS while keeping track of coordinates, update dictionary

with x coordinate as key and list of node values as value

Sort the keys, and append the values to a list.

Time complexity: O(nLogn)
Space complexity: O(n)

'''

def verticalTraversal(root):

  my_dict = {}
  def dfs(node, x, y):
    if not node:
      return
    
    if x not in my_dict:
      my_dict[x] = []

    my_dict[x].append((abs(y), node.val))
    
    dfs(node.left, x-1, y+1)
    
    dfs(node.right, x+1, y+1)

  dfs(root,0, 0)
  keys = list(my_dict.keys())
  keys.sort()

  '''
  this is n log n bc at worst, you just sort all the nodes in the tree
  '''
  
  for key in keys:
    my_dict[key].sort()

  
  ans = []
  for key in keys:
    report = []
    for tup in my_dict[key]:
      report.append(tup[1])
    ans.append(report)

  return ans

