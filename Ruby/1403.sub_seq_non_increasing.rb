# Given the array nums, obtain a subsequence of the array whose sum of elements 
# is strictly greater than the sum of the non included elements in such subsequence. 

# If there are multiple solutions, return the subsequence with minimum size 
# and if there still exist multiple solutions, 
# return the subsequence with the maximum total sum of all its elements. 
# A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

# Note that the solution with the given constraints is guaranteed to be unique. 
# Also return the answer sorted in non-increasing order.

def min_subsequence(nums)
    sorted = nums.sort
    left = sorted.inject(:+)
    right = 0
    i = 0
    while i < nums.length
        left -= sorted[i]
        right += sorted[i]

        if left < right
            return sorted.drop(i-a1).sort.reverse
        end
        i += 1
    end
    return []
end

x = [4,4,7,6,7]

p min_subsequence(x)