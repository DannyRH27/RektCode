def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """

    # Write your code here!
    zeroes, ones, twos = 0, 0, 0

    for n in lst:
        if n is 0:
            zeroes += 1
        if n is 1:
            ones += 1
        if n is 2:
            twos += 1

    for i in range(0, zeroes):
        lst[i] = 0

    for i in range(zeroes, zeroes + ones):
        lst[i] = 1

    for i in range(zeroes + ones, zeroes + ones + twos):
        lst[i] = 2

    return lst
