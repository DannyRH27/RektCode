def memoize(fn):
  input_to_output = {}
  def wrapper(*args):
    if args in input_to_output:
      return input_to_output[args]

    result = fn(*args)
    input_to_output[args] = result
    return result
  return wrapper

def print_input_and_output(fn):
	def wrapper(*args, **kwargs):
		print(args)
		result = fn(*args, **kwargs)
		print(result)
	return wrapper
		
@print_input_and_output
def add(one, two, keyword=True):
	return one+two

@print_input_and_output
def subtract(one, two, keyword=True):
	return one-two

# @memoize
import functools

@functools.lru_cache(128)
def fibonacci(n):
  if n == 0 or n == 1: return 1
  return fibonacci(n-1) + fibonacci(n-2)

import time
start = time.time()
print(fibonacci(100), time.time() - start)
