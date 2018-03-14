

def compress(input):
    if not input:
        return input

    modified = input.lower().replace(' ', '')
    count = 0
    output = []

    for index in range(len(modified)):
        count += 1
        if(
            index + 1 == len(modified) or
            modified[index] != modified[index + 1]
        ):
            output.append(modified[index])
            output.append(str(count))
            count = 0

    compressed = ''.join(output)
    return compressed if len(compressed) < len(modified) else modified
