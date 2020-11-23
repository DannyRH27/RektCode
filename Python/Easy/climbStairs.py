from functools import lru_cache

class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n < 2:
          return 1

        result = self.climbStairs(n-1) + self.climbStairs(n-2)

        return result
