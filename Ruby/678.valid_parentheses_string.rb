def check_valid_string(s)
    balance = 0
    i = 0
    while i < s.length
        if s[i] == '(' || s[i] == '{' || s[i] == '[' || s[i] == '*'
            balance +=1
        else
            balance -=1
        end
        i+=1
        if balance < 0
            return false
        end
    end

    return true if balance == 0

    balance = 0
    i = s.length - 1

    while i < s.length
        if s[i] == ')' || s[i] == '}' || s[i] == ']' || s[i] == '*'
            balance +=1
        else
            balance -=1
        end
        i+=1
        if balance < 0
            return false
        end
    end

    return true;
end