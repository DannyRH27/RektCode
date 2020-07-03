# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
def max_sub_array(nums)
    abs_max = nums[-1]
    curr_max = 0
    for i in 0..nums.length-1
        curr_max = curr_max + nums[i]
        if abs_max < curr_max
            abs_max = curr_max
        end
        if curr_max < 0
            curr_max = 0
        end
    end
    abs_max
    
end