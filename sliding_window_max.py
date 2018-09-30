from collections import deque


def max_window(nums, k):
    q = deque()
    output = []

    for i in range(len(nums)):
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        q.append(i)

        if i >= k - 1:
            output.append(nums[q[0]])

        while q and q[0] <= i - k + 1:
            q.popleft()

    return output
