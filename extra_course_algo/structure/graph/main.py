import matplotlib.pyplot as plt
import networkx as nx

#прелставление графа с помощью список смужности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# создать обьект графа
G = nx.Graph(graph)

# spring_layout - плоскость на которой мы будем рисовать
# seed - убрать рандом
plt.figure(figsize=(6,6))
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_size=700,
    node_color='skyblue',
    font_size=15,
    width=2
)
plt.show()