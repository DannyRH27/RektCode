from collections import deque


def detect_cycle(g):
  queue = deque()
  queue.append((g.array[0].head_node.data, -1))
  visited = set()
  visited.add(g.array[0].head_node.data)
  count = 0
  while len(queue):
    current, parent = queue.popleft()
    temp = g.array[current].head_node
    while temp:
        if temp.data not in visited:
            visited.add(temp.data)
            queue.append((temp.data, current))
        elif temp.data != parent:
            return True
        temp = temp.next_element
  return False
