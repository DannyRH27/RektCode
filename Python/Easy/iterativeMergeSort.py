def merge_lists(lst1, lst2):
    # Write your code here
    if not lst1 and not lst2:
        return []
    elif not lst1 and lst2:
        return lst2
    elif not lst2 and lst1:
        return lst1
    total_length = len(lst1) + len(lst2)
    new_list = [None] * total_length
    pointer = total_length - 1

    while lst1 and lst2:
        num1 = lst1[-1]
        num2 = lst2[-1]
        if num1 > num2:
            new_list[pointer] = lst1.pop()
            pointer -= 1
        elif num2 > num1:
            new_list[pointer] = lst2.pop()
            pointer -= 1
        elif num2 == num1:
            new_list[pointer] = lst1.pop()
            pointer -= 1 
            new_list[pointer] = lst2.pop()
            pointer -= 1 
    if lst1:
        new_list[0:len(lst1)] = lst1
    elif lst2:
        new_list[0:len(lst2)] = lst2
    return new_list
x = [1, 2, 3]
y = [4, 5, 6]
print(merge_lists(x, y), x, y)
