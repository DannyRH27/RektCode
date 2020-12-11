'''
non negative int, can swap two digits once at most to get the max value number,
return max value number

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]

I want the digits to be in descending order
finding the biggest digit and making sure it is on the left,

convert the num to str, and then split into an arr
iterate through arr and convert to ints and store in dict where key - int and value = index

max heapify this arr,
i'll have counter to see which index starting with 0

heappop and check if index == counter:
  increment counter by 1

until the arr is empty

if it is not equal to counter (not in the right place):
  then i swap, and that's my biggest number
  break

convert back to str
join
convert to int

'''
import heapq
from collections import deque
def maximumSwap(num):
  if num == 0:
    return num

  str_num = str(num)
  str_arr = list(str_num)

  my_dict = {}
  for i in range(len(str_arr)):
    n = int(str_arr[i])
    str_arr[i] = n
    if n in my_dict:
      my_dict[n].append(i)
    else:
      my_dict[n] = deque([i])

  copy = str_arr.copy()
  heapq._heapify_max(copy)

  idx = 0
  # print(my_dict)
  while len(copy):
    # print(copy)
    largest = heapq._heappop_max(copy)

    if largest == str_arr[idx]:
      my_dict[largest].popleft()
      idx += 1
    else:
      check_idx = my_dict[largest].pop()
      temp = str_arr[idx]

      str_arr[check_idx] = temp
      str_arr[idx] = largest
      break

  for i in range(len(str_arr)):
    str_arr[i] = str(str_arr[i])
  ans = int("".join(str_arr))

  return ans

# assert(maximumSwap(2736) == 7236)
# assert(maximumSwap(9973) == 9973)
assert(maximumSwap(98368) == 98863)
assert(maximumSwap(1993) == 9913  )
