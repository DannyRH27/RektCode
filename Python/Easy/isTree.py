def is_tree(g):
    # Write your code here

    return detect_cycle(g) is not True and find_mother_vertex(g) is not -1


def find_mother_vertex(g):
    # Write - Your - Code
    num_vertices_reached = 0

    for i in range(g.vertices):
        num_vertices_reached = DFS(g, i)
        if num_vertices_reached == g.vertices:
            return i

    return -1
# Create helper functions here


def DFS(g, source):
    visited = set()
    stack = [source]
    count = 0
    while len(stack):
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        count += 1
        temp = g.array[current].head_node
        while temp:
            stack.append(temp.data)
            temp = temp.next_element
    return count


def detect_cycle(g):
  queue = deque()
  queue.append((g.array[0].head_node.data, -1))
  visited = set()
  visited.add(g.array[0].head_node.data)

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
