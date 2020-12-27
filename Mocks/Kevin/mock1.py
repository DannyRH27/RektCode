'''
binary search

KNOW my exit condition
How do you know you have found the pivot???
if the number after is smaller
no dups
arr is sorted

arr is sorted, but pivots at a certain point

given arr, target

time complexity to target is still log n

return index of the target
Not in there, return -1

[5,6,0,1,2,3,4], 2
[6,8,2,5], 2
return 0

mid = 3

mid_val = 1

I was searching on the values
if search val is smaller than 
right = mid

if search val is greater 

mid = 1

if it is bigger than left:
  left = mid 

i'll know if it's pivoted if the first number is greater than the last number

normally bsearch if not pivoted

Key insights:

one to find out where the pivot occurs,
Bsearch to find pivot:
how should you move left and right?
if at any point, i find target, return index
mid is greater than left
mid is less than left


i know if the target exists, it's either going to be after the pivot or before the pivot

if my target is greater than my first element, then i search in 
list[pivot:]

otherwise, i need to search in smaller numbers
list[:pivot], return -1

'''
import math
def search(arr,target):

  # def find_pivot():

  
  pivot_idx = find_pivot()

  def bsearch(left, right):
    if left > right:
      return -1 
    mid = int(math.floor((left / 2) + (right / 2)))

    if arr[mid] == target:
      return mid


    # [1,2,3,4,5,6,7,8] , 3
    # [5,6,7,8,1,2,3,4], 4

    if arr[mid] > target:
      bsearch(left, mid-1)
    else:
      bsearch(mid+1, right)

  if target > arr[0]:
    ans = bsearch(pivot_idx,len(arr)-1)
  else:
    ans = bsearch(0, pivot_idx-1)
  
  return ans
    
