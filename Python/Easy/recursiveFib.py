from functools import lru_cache
@lru_cache
def fib(self, N: int) -> int:

      if N < 2:
        return N

      result = self.fib(N-1) + self.fib(N-2)
      return result
