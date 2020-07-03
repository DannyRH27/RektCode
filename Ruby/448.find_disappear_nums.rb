def find_disappeared_numbers(nums)
    res = []
    hash = {}

    nums.each do |num|
        hash[num] = 1
    end
    (1..nums.length).each do |i|
        res << i if !hash.has_key?(i)
    end
    return res
end