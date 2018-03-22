def rotate_matrix(matrix):
    dimension = len(matrix)

    for layer in range(dimension // 2):
        for i in range(dimension - 1 - 2 * layer):
            top = matrix[layer][layer + i]
            right = matrix[layer + i][dimension - 1 - layer]
            bottom = matrix[dimension - 1 - layer][dimension - 1 - i - layer]
            left = matrix[dimension - 1 - layer - i][layer]

            matrix[layer][layer + i] = left
            matrix[layer + i][dimension - 1 - layer] = top
            matrix[dimension - 1 - layer][dimension - 1 - i - layer] = right
            matrix[dimension - 1 - layer - i][layer] = bottom

    return matrix
