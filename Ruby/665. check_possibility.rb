
def check_possibility(nums)
    return false if  nums.nil?
    return true if non_decreasing?(nums)
    i = 0

    while i < nums.length - 1
        if nums[i] <= nums[i+1]
            i+=1
            next
        end
        
        if i > 0
            dup = nums.dup
            dup[i] = dup[i-1]
            if non_decreasing?(dup)
                return true
            end
        end
        if i < nums.length - 1
            dup = nums.dup
            dup[i] = dup[i+1]
            if non_decreasing?(dup)
                return true
            end
        end
        if i + 1 < nums.length - 1
            dup = nums.dup
            dup[i+1] = dup[i+2]
            if non_decreasing?(dup)
                return true
            end
        end
        dup = nums.dup
        dup[i+1] = dup[i]
        if non_decreasing?(dup)
            return true
        end
        i+=1
    end
    return false
end


def non_decreasing?(nums)
    i = 0

    while i < nums.length - 1
        if nums[i] > nums[i+1]
            return false
        end
        i+=1
    end
    return true
end

p check_possibility([1])