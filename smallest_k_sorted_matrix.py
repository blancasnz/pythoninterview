import heapq


def smallest_k(matrix, k):
    """
    Given a sorted matrix return smallest kth item.
    O(klogn)
    """
    h = [(row[0], row, 0) for row in matrix]
    heapq.heapify(h)

    for _ in range(k-1):
        val, row, index = heapq.heappop(h)
        if index + 1 < len(row):
            heapq.heappush(h, (row[index+1], row, index+1))
    return h[0][0]
