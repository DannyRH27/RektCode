def searchMatrix(matrix, target):
  row = len(matrix) - 1
  col = 0

  while row >= 0 and col < len(matrix[0]):
    if matrix[row][col] > target:
      row -=1
    elif matrix[row][col] < target:
      col +=1
    else:
      return True
  return False


def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Write your code here!
    if len(lst) is 0 or len(lst[0]) is 0:
        return False
    start = 0
    end = len(lst)-1

    while start <= end:
        row = (start + end) // 2
        check_start = lst[row][0]
        check_end = lst[row][-1]
        if number == check_start or number == check_end:
            return True
        if number > check_start and number < check_end:
            break
        elif number < check_start and row > 0:
            end = row - 1
        elif number > check_end and row < len(lst)-1:
            start = row + 1
        else:
          break

    start = 0
    end = len(lst[0])-1

    while start <= end:
        mid = (start + end) // 2
        if lst[row][mid] == number:
            return True
        if lst[row][mid] > number:
            end = mid - 1
        if lst[row][mid] < number:
            start = mid + 1

    return False
