def two_sum(nums, target)
    hash = Hash.new(0)
    arr = []
    nums.each.with_index do |num, idx|
        if !hash.keys.include?(target-num)
            hash[num] = idx
        elsif hash.keys.include?(target-num)
            arr << idx
            arr << hash[target-num]
            break
        end
    end
    return arr
end