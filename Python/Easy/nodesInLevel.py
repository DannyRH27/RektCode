from collections import Counter, deque


def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    # Write your code here!
    visited = Counter()
    root = 0
    visited[root] = 1
    q = deque()
    q.append(root)

    while q:
        entry = q.popleft()

        node = graph.graph[entry]

        while node is not None:
            data = node.vertex
            if data not in visited:
                visited[data] = visited[entry] + 1
                q.append(data)
            node = node.next

    ans = 0

    for i in range(len(graph.graph)):
        if visited[i] == level:
            ans += 1

    return ans
