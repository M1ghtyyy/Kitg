
def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def find_connected_components(graph, num_nodes):
    visited = [False] * num_nodes
    components = []

    for node in range(num_nodes):
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)

    return components

num_nodes = 6
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2],
    4: [5],
    5: [4]
}

print(find_connected_components(graph, num_nodes)) # output -> [[0, 1, 2, 3], [4, 5]]