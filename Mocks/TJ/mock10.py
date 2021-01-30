'''
game of life
board m x n grid

each cell has initial state 1 or dead 0

8 neighbors
4 Rules:
any live cell with fewer than 2 live neighbors dies from underpopulation
any live cell with 2 or 3 live neighbors lives on to next gen
any live cell with more than 3 live neighbors dies from overpopulation
any dead cell with exactly 3 live neighbors becomes a live cell as if by reproduction

Goal is to take in a board that has a first state, return the next state.

visited set

Spending extra memory
new grid = [[]]
recurse(check the state of the cell)
  these are all my neighbors
  count live ones

  current cell rules

  recurse()
  state change after


in place

iteratively

previously: i iterate through, check neighbors and then i flip state
need to know the original state of the neighbors while i'm changing each cell

[
 [2 1 1]
 [1 1 1]
 [1 1 0]
]

let's say it was dead and it's going turn alive, i'll change this number to a 2
if it was alive, but will now be dead, i'll change this number to a 3

now on the second pass, i can now check if it's a 0 or a 2 to know it is/was dead
i know a 1 or a 3 is/was alive

on the second pass, now i can try to go through and just fix everything

'''