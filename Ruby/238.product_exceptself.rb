require 'byebug'
def product_except_self(nums)
    ans = [1]
    # Calculate the left side values
    (1..(nums.length - 1)).each do |i|
       ans[i] = ans[i-1] * nums[i-1] 
    end
    
    r = 1
   # Calculate right side values
    ((nums.length-1).downto(0)).each do |i|
        ans[i] *= r
        r *= nums[i]
    end
    ans
end

x = [1,2,3,4]
p product_except_self(x)
# Output: [24,12,8,6]
