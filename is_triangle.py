

def is_triangle(a, b, c):
    output = []
    for A, B, C in zip(a, b, c):
        if (A + B > C) and (A + C > B) and (B + C > A):
            output.append('Yes')
        else:
            output.append('No')
    return output
