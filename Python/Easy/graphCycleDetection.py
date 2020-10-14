from collections import deque
def detect_cycle(g):
  # Write your code here
  visited = set()
  queue = deque()
  queue.append(g.array[0].head_node.data)

  while len(queue):
    current = queue.popleft()
    if current in visited:
      continue

    visited.add(current)
    temp = g.array[current].head_node
    while temp:
      if temp.data in visited:
        return True

      queue.append(temp.data)
      temp = temp.next_element
  return False
