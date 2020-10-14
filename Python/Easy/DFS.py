def dfs_traversal(g, source):
    result = ""

    if g.vertices is 0:
        return result

    visited = set()
    stack = []
    stack.append(source)
    visited.add(source)

    while len(stack):
        current = stack.pop()
        result += str(current)
        temp = g.array[current].head_node
        while temp:
            if temp.data not in visited:
                stack.append(temp.data)
                visited.add(temp.data)
            temp = temp.next_element

    return result


