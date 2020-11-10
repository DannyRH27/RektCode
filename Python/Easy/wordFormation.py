def is_formation_possible(lst, word):
    # Write your code here
    my_dict = {}

    for n in lst:
        my_dict[n] = True

    for i in range(1, len(word)):
        first = word[0:i]
        second = word[i:len(word)]
        check1 = False
        check2 = False

        if first in my_dict:
            check1 = True

        if second in my_dict:
            check2 = True

        if check1 and check2:
            return True
    return False
