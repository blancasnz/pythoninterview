

def compress(input):
    if not input:
        return input

    modified_input = input.lower().replace(' ', '')
    current = modified_input[0]
    count = 1
    output = []

    for index in range(1, len(modified_input) + 1):
        if(
            index == len(modified_input) or
            modified_input[index] != current
        ):
            output.append(current)
            if count > 1:
                output.append(str(count))
            if index < len(modified_input):
                current = modified_input[index]
            count = 1
        else:
            count += 1

    return ''.join(output)
