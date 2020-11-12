import heapq


def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """

    # Write your code here!
    heapq.heapify(pipes)
    total = 0

    while len(pipes) > 1:
        first = heapq.heappop(pipes)
        second = heapq.heappop(pipes)

        total += first + second
        heapq.heappush(pipes, first+second)

    return total
