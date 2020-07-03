def find_lucky(arr)
    
    hash = Hash.new(0)
    arr.each {|num| hash[num] += 1}
    
    lucky = []
    
    hash.each do |k,v|
        if k == v 
            lucky << k
        end
    end
    
    lucky.sort!
    if lucky.empty?
        return -1
    end
    return lucky[-1]
end