def dfs_iterative(graph, start_vertex):
    visited = set()

    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end = ' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

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

dfs_iterative(get_graph(), 'A')