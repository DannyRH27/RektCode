def searchInSortedMatrix(matrix, target):
    # Write your code here.

	row = 0
	col = len(matrix[0]) - 1

	while col >= 0:
		potentialMatch = matrix[row][col]
		if target == potentialMatch:
			return [row, col]
		elif target > potentialMatch:
			row += 1
		elif target < potentialMatch:
			col -= 1

	return [-1, -1]
