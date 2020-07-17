def isValidSubsequence(array, sequence):
    # Write your code here.
	# two pointers, counter
	# iterate through the main array
	# keep track of the first in sequence
	# move to next if found and increment counter
	# if we reach the end of the sequence, return true, else return false

	count = 0
	i = 0

	for n in array:
		if i == len(sequence):
			break
		if sequence[i] == n:
			count += 1
			i += 1

	return count == len(sequence)
