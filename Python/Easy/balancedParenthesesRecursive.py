def balanced(testVariable, startIndex=0, currentIndex=0):

  def recursive_helper(testVariable, currentIndex, open_count, close_count):
    print(currentIndex, len(testVariable))
    if currentIndex == len(testVariable):
      return True

    if testVariable[currentIndex] == "(":
      open_count += 1

    if testVariable[currentIndex] == ")":
      close_count += 1

    if close_count > open_count:
      return False
    return recursive_helper(testVariable, currentIndex + 1, open_count, close_count)
  return recursive_helper(testVariable, currentIndex, 0, 0)
