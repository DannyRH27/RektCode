def hasPathSum(self, root: TreeNode, sum: int) -> bool:
  if not root:
    return False
  check = set()
  def dfs(node, total):

    if not node.left and not node.right:
      total += node.val
      check.add(total)
      return

    total += node.val
    if node.left:
      dfs(node.left, total)
    if node.right:
      dfs(node.right, total)

  dfs(root, 0)

  if sum in check:
    return True
  return False
