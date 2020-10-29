def generate(numRows):
  pascal = []

  if numRows == 0:
      return pascal

  count = 0

  while count < numRows:
      newList = []

      if count == 0:
          newList = [1]
      else:
          newListLength = len(prevList) + 1
          for i in range(0, newListLength):
              if i == 0 or i == newListLength-1:
                  newEle = 1
              else:
                  newEle = prevList[i] + prevList[i-1]
              newList.append(newEle)
      pascal.append(newList)
      prevList = newList
      count += 1
  return pascal
