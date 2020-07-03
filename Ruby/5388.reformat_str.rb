def reformat(s)
    arr = s.split("")
    alpha = "abcdefghijklmnopqrstuvwxyz"
    nums = "1234567890"
    count_num = 0
    count_alpha = 0
    numbers = []
    letters = []
    arr.each do |ele|
        if nums.include?(ele)
            numbers << ele
            count_num += 1
        elsif alpha.include?(ele)
            letters << ele
            count_alpha +=1
        end
    end

    if count_num - count_alpha >= 2 || count_alpha - count_num >=2
        return ""
    end

    sorted = arr.sort
    valid = []
    while valid.length < sorted.length
        if letters.length > numbers.length
            valid.unshift(letters.shift)
            valid.unshift(numbers.shift)
        else
            valid.unshift(numbers.shift)
            valid.unshift(letters.shift)
        end
    end
    
    valid.delete(nil)

    return valid.join("")

end


s = "a0b1c2"
p reformat(s) 
# Output: "c2o0v1i9d"