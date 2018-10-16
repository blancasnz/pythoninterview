

def fill(image, start_y, start_x, new_color):
    visited = set()
    dfs(image, start_y, start_x, image[start_y][start_x], new_color, visited)
    return image


def dfs(image, y, x, old_color, new_color, visited):
    if (y, x) in visited:
        return
    if not (0 <= y <= len(image) - 1):
        return
    if not (0 <= x <= len(image[0]) - 1):
        return

    visited.add((y, x))

    if image[y][x] == old_color:
        image[y][x] = new_color

        dfs(image, y + 1, x, old_color, new_color, visited)
        dfs(image, y, x + 1, old_color, new_color, visited)
        dfs(image, y - 1, x, old_color, new_color, visited)
        dfs(image, y, x - 1, old_color, new_color, visited)
