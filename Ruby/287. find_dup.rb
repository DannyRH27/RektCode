def find_duplicate(nums)
    hash = Hash.new(0)
    nums.each do |num|
        hash[num] += 1
    end
    hash.each do |k, v|
        return k if v > 1
    end
end