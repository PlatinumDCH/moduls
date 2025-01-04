import networkx as nx

import matplotlib.pyplot as plt


graph = nx.Graph()

graph.add_node('Dima')
graph.add_node('Vika')
graph.add_node('Natalia')
graph.add_node('Volodia')

graph.add_edge('Dima', 'Vika')
graph.add_edge('Natalia', 'Dima')
graph.add_edge('Volodia', 'Vika')
graph.add_edge('Volodia', 'Dima')

nx.draw(graph, with_labels=True)
plt.axis('off')
plt.show
