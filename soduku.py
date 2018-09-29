
def valid_sodoku(board):
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            if board[i][j] in row_set:
                return False
            if board[j][i] in col_set:
                return False

            if board[i][j] != '.':
                row_set.add(board[i][j])
            if board[j][i] != '.':
                col_set.add(board[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block_set = set()
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if board[k][l] == '.':
                        continue
                    if board[k][l] in block_set:
                        return False
                    block_set.add(board[k][l])
    return True
