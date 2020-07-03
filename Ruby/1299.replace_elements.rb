# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.


def replace_elements(arr)
  i = arr.length - 1
  max = arr.last
  while i >= 0
    if i == arr.length - 1 
      arr[i] = -1
    else
      temp = arr[i]
      arr[i] = max
      max = temp if temp > max
    end
    i -= 1
  end

  return arr
end

x = [17,18,5,4,6,1]
p replace_elements(x)
# Output: [18,6,6,6,1,-1]