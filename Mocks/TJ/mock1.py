# 4:39

# N Rooms, start in room 0
# Each room has a distinct number all the way to n-1, indices
# Each room may have some keys to access another room (pointer)
# All rooms start locked, except for room 0
# Can walk back and forth between rooms freely
# Return true if you can enter every room
# input is 2d array, outer array is array of keys you find in the room

# Example 1:

"""
Input: [[1], [2], [3], []]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1, 3], [3, 0, 1], [2], [0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""

"""
I know there are N rooms
Every time i enter a room, i will add all keys to a set
Have a visited set to see which rooms i've already hit
O(ROOMS + KEYS)
O(N + M)
"""



"""
Start in room 0
take keys from room 0 and make a set for keys
do keys = range(1, n)
"""


def canVisitAllRooms(rooms):

  if len(rooms) == 1:
    return True
  visited = set([0])
  keys = set()

  def searchRoom(room):
    for key in room:
      if key != 0 and key not in visited:
        keys.add(key)
        visited.add(key)
        searchRoom(rooms[key])

  searchRoom(rooms[0])
  return len(keys) == len(rooms)-1

  """
  Could start with the key of 0 already in the keys set
  then use one set for keys and visited

  Could restructure to have key argument instead of room and use rooms[key]
  """



  



  
