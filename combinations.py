
def generate(n, k, index, path, output):
    if len(path) == k:
        output.append(path)

    for i in range(index, n+1):
        generate(n, k, i+1, path + [i], output)


def combinations(n, k):
    output = []
    generate(n, k, 1, [], output)
    return output
