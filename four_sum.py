

def four_sum(A, B, C, D):

    sums = {}

    for a in A:
        for b in B:
            if a + b in sums:
                sums[a+b] += 1
            else:
                sums[a+b] = 1

    counts = 0
    for c in C:
        for d in D:
            if -c - d in sums:
                counts += sums[-c-d]
    return counts
