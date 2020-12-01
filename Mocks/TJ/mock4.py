'''
total of numCourses labeled from 0 to numCourses - 1
some courses may have prerequisites, [(1,0)]
in order to take course 1, must take course 0
given total numCourses and all possible prereq pairs, is it possible to finish all courses
canFinish(2,[[1,0]]) == True 

No prereqs duplicated

graph of edges, and i want to know, can i hit all of the vertices
could be multiple entry points
first, i need a list or set of all prereqs needed.
then, i need a list or set of all available entry point courses initially.
As i go through, i can add to my available courses able to be taken if i have an entry point.

If the length of available set is equal to numCourses, then return true
otherwise return false
'''

from collections import deque
def canFinish(numCourses, prerequisites):

  adj = {}
  adj2 = {}
  
  # Add all prereqs as keys and the courses that need it, as values
  for i in range(numCourses):
    adj[i] = set()
    adj2[i] = set()

  for pair in prerequisites:
    course, prereq = pair

    adj[course].add(prereq)
    adj2[prereq].add(course)

  available = deque()
  # add the courses that have no prereqs
  for course in range(numCourses):
    if len(adj[course]) == 0:
      available.append(course)

  taken = set()
  while len(available):
    course = available.popleft()
    if course in taken:
      continue
    taken.add(course)
    must_modify = adj2[course]
    for modify in must_modify:
      if modify in adj:
        adj[modify].remove(course)
        if len(adj[modify]) == 0:
          available.append(modify)
          del adj[modify]
  

  return len(taken) == numCourses



assert(canFinish(2, [[1, 0]]) == True)
assert(canFinish(3, [[0, 1], [0, 2], [1, 0]]) == False)
