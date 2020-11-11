def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = set()  # A list to store duplicates

    # Write your code here!
    visited = set()
    for n in lst:
        if n in visited:
            result.add(n)
        visited.add(n)
    result = list(result)
    return result
