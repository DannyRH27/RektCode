# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: 
# Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.


def is_happy(n)
    
    tested = Set.new
    sum = n
    until sum == 1
        sum = sum.digits.map{|x| x.to_i ** 2}.inject(:+)
        if tested.include?(sum)
            return false
        end
        tested.add(sum)
    end
    return sum == 1

end

y = 19
puts 19.is_happy()

x = 82
x ="82"
x = ["8", "2"]
x = [64, 4]
x = 68
puts x.split(" ")