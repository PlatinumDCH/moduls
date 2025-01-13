
def dfs_recursive(graph, vetrex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vetrex)
    print(vetrex, end=' ') # заходим в узел
    for neighbor in graph[vetrex]:
        if neighbor not in visited:
            dfs_recursive(graph,neighbor,visited)


def get_graph():
    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
    return graph

dfs_recursive(get_graph(), "C")