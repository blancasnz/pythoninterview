
def look_and_say(n):
    """
    1
    11
    21
    1211
    111221
    312211
    13112221
    1113213211
    31131211131221
    13211311123113112211
    etc...
    """

    seq = "1"
    output = [seq]
    for _ in range(1, n):
        seq = sequence(seq)
        output.append(seq)

    return output


def sequence(sequence):
    current = sequence[0]
    count = 1
    output = []

    for index in range(1, len(sequence) + 1):
        if index == len(sequence):
            output.append(str(count))
            output.append(current)
            break

        if sequence[index] == current:
            count += 1

        if sequence[index] != current:
            output.append(str(count))
            output.append(current)
            current = sequence[index]
            count = 1

    return ''.join(output)
