def preorderTraversal(root):
  if root == None:
    return []
  arr = []
  stack = [root]

  while stack:
    root = stack.pop()
    if root != None:
      arr.append(root.val)

    if root.right != None:
      stack.append(root.right)
    if root.left != None:
      stack.append(root.left)

  return arr
