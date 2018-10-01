
def find_paths(graph):
    output = []
    dfs(graph, 0, [0], output)
    return output


def dfs(graph, start, path, output):
    if start == len(graph) - 1:
        output.append(path)

    for neighbor in graph[start]:
        dfs(graph, neighbor, path + [neighbor], output)
