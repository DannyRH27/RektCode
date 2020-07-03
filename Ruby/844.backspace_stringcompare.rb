def backspace_compare(s, t)
    
    return process_str(s) == process_str(t)
end

def process_str(str)
    w = 0
    str.each_char.with_index do |char, i|
        if char == "#"
            w -= 1 if w > 0 
        else
            str[w] = char
            w += 1
        end
    end

    return str[0...w]
end

s = "a#c"
t = "b"
p process_str(s)
p process_str(t)
p backspace_compare(s,t)