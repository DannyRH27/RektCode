# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 
# 
# 
# how do i figure out if it is an anagram
# initalize hash with empty arrays as values
# iterate through array of strings
# set letters of string as a hash count for key values and the string should be pushed into the array corresponding with those letters
# return an array of all values

def group_anagrams(strs)
    result = Hash.new{|h,k| h[k] = []}
    strs.each do |str|
        hash = Hash.new(0)
        str.each_char do |char|
            hash[char] +=1
        end
        result[hash] << str
    end
    return result.values
end

# alternatively could sort each string as and use sorted string as a key