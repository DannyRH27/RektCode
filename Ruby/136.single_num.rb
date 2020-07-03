def single_number(nums)

    x = 0
    
    nums.each do |num|
        x ^= num
    end
    
    return x
end