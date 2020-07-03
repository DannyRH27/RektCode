# Given a sorted array nums, remove the duplicates in-place such that each element appear only once 
# and return the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

def remove_duplicates(nums)
    prev = nil
    count = 0
    nums.each do |num|
        if num == prev
            next
        else
            nums[count] = num
            prev = num
            count+=1
        end
    end

    return count
end

x = [0,1,2,3,4,5,5]

p remove_duplicates(x)