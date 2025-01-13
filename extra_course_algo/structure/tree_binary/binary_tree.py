import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret
    
def insert(root: Node, key):
    if root is None:
        return Node(key)
    # if key == root.val:
    #     return root
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def get_tree(Node):
    root = Node(5)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 4)

    root = insert(root, 8)
    root = insert(root, 8.5)
    root = insert(root, 1)
    root = insert(root, 7.5)
    root = insert(root, 7.4)
    root = insert(root, 7.6)

    root = insert(root, 8.4)
    root = insert(root, 8.6)

    return root

def add_edges(graph, node, pos, x=0,y=0, layer=1):
    if node is not None:
        graph.add_node(node.val)
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root:Node):
    tree = nx.DiGraph()
    pos = {tree_root.val: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color="skyblue")
    plt.show()

    plt.show()

root = get_tree(Node)
draw_tree(root)