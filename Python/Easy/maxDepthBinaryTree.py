from functools import lru_cache


class Solution:
    @lru_cache
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, depth):

          if node is None:
            return depth
          left = helper(node.left, depth + 1)
          right = helper(node.right, depth + 1)
          return max(left, right)

        return helper(root, 0)
