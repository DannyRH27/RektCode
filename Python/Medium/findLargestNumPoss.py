def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    # Write your code here!
    if sum_of_digits / 9.0 > number_of_digits:
        return [-1]
    res = []
    total = sum_of_digits
    while total >= 0 and len(res) < number_of_digits:
        if total > 9:
            res.append(9)
            total -= 9
        else:
            res.append(total)
            total -= total

    return res

assert(find_largest_number(3, 20) == [9,9,2])
assert(find_largest_number(3, 27) == [9,9,9])
assert(find_largest_number(3, 28) == [-1])
print("All test cases passed!")
