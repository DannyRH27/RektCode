def reverse(x)
    rev = x.to_s.split("")
    
    if x % 10 == 0
        rev.pop
    end
    
    rev = rev.reverse.join("").to_i
    
    if x.negative?
        rev *= -1
    end
    return 0 if rev > (2**31) - 1 || rev < -2**31
    return rev
end
