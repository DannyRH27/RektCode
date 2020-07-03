# Given an array of string words. 
# Return all strings in words which is substring of another word in any order. 

# String words[i] is substring of words[j], 
# if can be obtained removing some characters to left and/or right side of words[j].

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.



def string_matching(words)
    output = []
    words.each.with_index do |word, i|
        words.each.with_index do |word, j|
            if words[i].include?(words[j]) && !output.include?(words[j]) && words[i] != words[j]
                output << words[j]
            end
        end
    end
    return output
end

x = ["mass","as","hero","superhero"]

p string_matching(x)