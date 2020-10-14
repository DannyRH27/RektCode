def check_path(g, source, destination):
    # Write your code here
    if g.vertices == 0:
        return False

    visited = set()
    queue = deque()
    queue.append(source)

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        if current == destination:
            return True
        visited.add(current)
        temp = g.array[current].head_node
        while temp:
            queue.append(temp.data)
            temp = temp.next_element
    return False
