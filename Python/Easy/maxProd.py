def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    # Write your code here!
    max1 = lst[0]
    max2 = lst[1]

    min1 = lst[0]
    min2 = lst[1]

    for i in range(len(lst)):
        if lst[i] > max1:
            max2 = max1
            max1 = lst[i]
        elif lst[i] > max2:
            max2 = lst[i]

        if lst[i] < min1:
            min2 = min1
            min1 = lst[i]
        elif lst[i] < min2:
            min2 = lst[i]

    min_prod = min1 * min2
    max_prod = max1 * max2

    if min_prod > max_prod:
        if min1 > min2:
            return min2, min1
        else:
            return min1, min2
    else:
        if max1 > max2:
            return max2, max1
        else:
            return max1, max2
