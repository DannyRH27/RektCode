'''
Given an array of non-negative integers arr, 
your task is to find the number of ways it can be split into three non-empty contiguous subarrays 
such that the sum of the elements in the first subarray is less than or equal 
to the sum of the elements in the second subarray, and the sum of the elements in the second subarray is less than or equal to
the sum of the elements in the third subarray.
first_sub <= second_sub <= third_sub
'''
'''
You are given a matrix of characters representing a big box. Each cell of the matrix contains one of three characters:

'.', which means that the cell is empty
'*', which means that the cell contains an obstacle
'#', which means that the cell contains a small box.
You decide to rotate the big box clockwise to see how the small boxes will fall under the gravity. 
After rotating, each small box falls down until it lands on an obstacle, another small box, or the bottom of the big box.

Given box, a matrix representation of the big box, your task is to return the state of the box after rotating it clockwise.



box = [['#', '#', '.', '.', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '#', '.']]
the output should be

rotateAndFall(box) = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.'],
                      ['#', '.', '.'],
                      ['#', '#', '.'],
                      ['#', '#', '#'],
                      ['#', '#', '#']]
box = [['#', '#', '.', '*', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '#', '.']]
the output should be

rotateAndFall(box) = [['.', '.', '.'],
                      ['.', '.', '#'],
                      ['.', '.', '#'],
                      ['#', '.', '*'],
                      ['#', '#', '.'],
                      ['#', '#', '.'],
                      ['#', '#', '.']]
'''