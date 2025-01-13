import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() #DiGraph

G.add_node("A")
G.add_nodes_from(['B','C','D'])
G.add_edge('A','B')
G.add_edges_from([('A', 'C'), ('B', 'C'), ('B', 'D')])

print(G.nodes()) # посмотерть вершины
print(G.edges()) # посмотреть ребра
print(list(G.neighbors('B'))) # посмотреть соседов

# G.remove_node('A')

"""
DG = nx.DiGraph(G)
DG.remove_edge('A', 'B')

DG.add_node(1)
DG.add_edge(1, 'A', weight=2.4, label='connection')
DG.nodes[1]['color'] = 'green'
"""

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