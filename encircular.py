
def is_circle(commands):
    simulation = commands * 4

    rotation = 0
    current = [0, 0]
    for com in simulation:
        if com == 'G':
            direction = abs(rotation) % 4
            if direction == 0:
                current[1] = current[1] + 1
            if direction == 1:
                current[0] = current[0] + 1
            if direction == 2:
                current[1] = current[1] - 1
            if direction == 3:
                current[0] = current[0] - 1

        if com == 'R':
            rotation += 1
        if com == 'L':
            rotation -= 1

    return current == [0, 0]


def does_circle_exist(commands):
    output = []
    for command in commands:
        if is_circle(command):
            output.append('YES')
        else:
            output.append('NO')
    return output
