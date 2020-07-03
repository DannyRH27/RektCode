def length_of_longest_substring(s)
    
    longest = 0
    hash = Hash.new(0)
    pointer = 0
    s.each_char.with_index do |char, idx|
        if !hash.keys.include?(char)
            hash[char] += 1
            if idx - pointer + 1 > longest
                longest = idx - pointer + 1
            end
        else
            until s[pointer] == char
                hash.delete(s[pointer])
                pointer += 1
            end
            
            pointer += 1
        end
    end
    return longest
end