'''
unsorted arr
return whether an increasing subsequence of length 3 exists in the arr or not.
TRUE OR FALSE MOTHAFUCKAA
Numbers can repeat
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false

Example 3:
Input: [3,1,4,2,4]
Output: true




'''


def increasingTriplet(nums):
  first = float('inf')
  second = float('inf')

  for n in nums:
    print(first,second)
    if n <= first:
      first = n
    elif n <= second:
      second = n
    else:
      return True
  return False


# assert(increasingTriplet([1, 2, 3, 4, 5]) ==  True)
assert(increasingTriplet([5, 4, 3, 2, 1]) == False)
