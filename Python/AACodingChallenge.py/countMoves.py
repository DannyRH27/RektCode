"""
Given an array of integers, determine the number of moves to make all elements equal
Choose n-1 elements during each move and increment or decrement each value by one
"""


def countMoves(numbers):
    # Write your code here
    if len(numbers) <= 1:
        return 0

    total = 0

    small = min(numbers)
    for i in range(len(numbers)):
        total += numbers[i]

    total = total - small * len(numbers)
    return total
