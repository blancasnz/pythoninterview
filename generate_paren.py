
def generate(output, current, left, right, n):
    if len(current) == 2 * n:
        output.append(current)
        return

    if left < n:
        generate(output, current + '(', left + 1, right, n)

    if left > right:
        generate(output, current + ')', left, right + 1, n)


def generate_parenthesis(n):
    output = []
    generate(output, '', 0, 0, n)
    return output
