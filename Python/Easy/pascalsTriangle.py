  def getRow(self, rowIndex: int) -> List[int]:
    def buildRow(rowIndex):
      if rowIndex == 0:
        return [1]

      if rowIndex == 1:
        return [1, 1]

      first = [1]
      last = [1]
      lst = []
      prevRow = buildRow(rowIndex-1)

      for i in range(1, rowIndex):
        print(i)
        num = prevRow[i] + prevRow[i-1]
        lst.append(num)

      return first + lst + last

    return buildRow(rowIndex)
