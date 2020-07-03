# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

# direction can be 0 (for left shift) or 1 (for right shift). 
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"
 
def string_shift(s, shift)
    s = s.split("")
    shift.each do |pair|
        if pair[0] == 0
            pair[1].times {
            shift = s.shift
            s.push(shift)
        }
        else
            pair[1].times {
                pop = s.pop
                s.unshift(pop)
            }
        end
    end
    return s.join("")
    
end

def string_shift2(s,shift)
    count_shift = 0
    s = s.split("")

    shift.each do |pair|
        if pair[0] == 0
            count_shift -= pair[1]
        else
            count_shift += pair[1]
        end
    end

    if count_shift == 0
        return s.join("")
    elsif count_shift < 0
        (count_shift*-1).times do 
            shift = s.shift
            s.push(shift)
        end
        return s.join("")
    else
        count_shift.times do
            pop = s.pop
                s.unshift(pop)
        end
        return s.join("")
    end
end

s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]] 
# Output: "efgabcd"
d = "abc"
shift2 = [[0,1],[1,2]]
# Output: "cab"
p string_shift2(s, shift)
p string_shift2(d, shift2)
# Constraints:



# 1 <= s.length <= 100
# s only contains lower case English letters.
# 1 <= shift.length <= 100
# shift[i].length == 2
# 0 <= shift[i][0] <= 1
# 0 <= shift[i][1] <= 100