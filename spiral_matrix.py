

def spiral_matrix(n):
    """
    Makes spiral nxn matrix.

    1   2  3   4
    12  13 14  5
    11  16 15  6
    10  9  8   7
    """

    if n < 1:
        raise ValueError()

    matrix = [[None] * n for _ in range(n)]

    current = 1
    row = 0
    column = 0
    direction = 0

    #     r   d   l  u
    # col 1   0  -1  0
    # row 0   1   0  1
    direction_increment = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while current <= n*n:

        matrix[row][column] = current
        current += 1

        col_dir, row_dir = direction_increment[direction]
        column += col_dir
        row += row_dir

        if (
            column == -1 or column == n or
            row == -1 or row == n or
            matrix[row][column] is not None
        ):
            col_dir, row_dir = direction_increment[direction]
            column -= col_dir
            row -= row_dir

            direction = (direction + 1) % 4

            col_dir, row_dir = direction_increment[direction]
            column += col_dir
            row += row_dir

    return matrix
