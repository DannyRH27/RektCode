def max_sub_array_of_size_k(k, arr):
  start, end = 0, k
  abs_total = sum(arr[:end])
  cur_total = abs_total

  while end < len(arr) - 1:
    cur_total += arr[end]
    cur_total -= arr[start]
    end += 1
    start += 1

    if cur_total > abs_total:
      abs_total = cur_total

  return abs_total
