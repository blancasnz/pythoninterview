
def consecutive(num):
    count = 0
    limit = num // 2 + 2
    for i in range(2, limit):
        k = num - (i - 1) * i / 2
        if k <= 0:
            return count
        if k % i == 0:
            count += 1
    return count
