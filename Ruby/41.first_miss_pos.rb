def first_missing_positive(nums)
 return 1 if nums.empty?
    i = 0
    while i < nums.length
        ele = nums[i]
        correct_index = ele-1
        if i == correct_index || nums[correct_index] == ele
            i += 1
        elsif ele > 0 && ele < nums.length
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else
            i += 1
        end 
    end
    j = 1
    while j <= nums.length
        return j if nums[j-1] != j
        j += 1
    end
    j
end