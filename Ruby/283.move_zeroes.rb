# Given an array nums, write a function to move all 0
# 's to the end of it while maintaining the 
# relative order of the non-zero elements.
def move_zeroes(nums)
    count = 0
    nums.each.with_index do |num, i|
        if num != 0
            nums[count] = num
            count += 1
        end
    end

    while count < nums.length
        nums[count] = 0
        count += 1
    end

    return nums
end

puts move_zeroes([0,1,0,3,12])
