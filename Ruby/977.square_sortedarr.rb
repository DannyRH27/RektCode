# Given an array of integers A sorted in non-decreasing order, 
# return an array of the squares of each number, also in sorted non-decreasing order.

def sorted_squares(a)
#     iterate through og array, grab neg nums, square them
#     create another array, holding pos squares
#     merging algorithm
  pos = []
  neg = []
  res = []

  a.each do |num|
    num > 0 ? pos.push(num ** 2) : neg.unshift(num ** 2)
  end

  while !pos.empty? && !neg.empty?
    if pos.first > neg.first
      res.push(neg.shift)
    else
      res.push(pos.shift)
    end
  end

  return res + pos + neg

end


x = [-4,-1,0,3,10]
p sorted_squares(x)

# Output: [0,1,9,16,100]

y = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
p sorted_squares(y)