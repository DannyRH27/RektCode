def bfs_traversal_helper(g, source):
    result = ""
    queue = deque()
    queue.append(source)
    visited = [False] * g.vertices
    visited[source] = True

    while len(queue) != 0:
        current = queue.popleft()
        result += str(current)
        temp = g.array[current].head_node
        while temp:
            if visited[temp.data] is False:
                queue.append(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result


def bfs_traversal(g, source):
    if g.vertices is 0:
        return ''

    return bfs_traversal_helper(g, 0)
