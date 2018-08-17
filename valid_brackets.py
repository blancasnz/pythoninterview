
def is_valid(s):
    brackets = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    stack = []

    for bracket in s:
        if bracket in brackets:
            stack.append(bracket)
        else:
            if len(stack) == 0 or brackets[stack.pop()] != bracket:
                return False

    return len(stack) == 0
