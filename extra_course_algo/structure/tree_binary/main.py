class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_travelsal(root:Node):
    r"""
    прямой обход дерева
               1
             /   \
            2     3
           / \   / \
          4   5 6   7
        
    [1, 2, 4, 5, 3, 6, 7]
    """
    if root is None:
        return []
        # 1. Посетить текущий узел
        # 2. Обойти левое поддерево
        # 3. Обойти правое поддерев
    return [root.value] + pre_order_travelsal(root.left) + pre_order_travelsal(root.right)

def preorder_reqursive(root: Node):
    if root is None:
        return 
    print(root.value)
    preorder_reqursive(root.left)
    preorder_reqursive(root.right)

def in_order_travelsal(node):
    r"""
    центровой обход
               1
             /   \
            2     3
           / \   / \
          4   5 6   7

        [4, 2, 5, 1, 6, 3, 7]
    """
    if node is None:
         return []
    # 1. Обойти левое поддерево
    # 2. Посетить текущий узел
    # 3. Обойти правое поддерево
    return in_order_travelsal(node.left) + [node.value] + in_order_travelsal(node.right)

def inorder_reqursive(root: Node):
    if root:
        inorder_reqursive(root.left)
        print(root.value)
        inorder_reqursive(root.right)

def post_order_traversal(node):
    r"""
    обратный обход
               1
             /   \
            2     3
           / \   / \
          4   5 6   7

        [4, 5, 2, 6, 7, 3, 1]
    """
    if node is None:
         return []
    # 1. Обойти левое поддерево
    # 2. Обойти правое поддерево
    # 3. Посетить текущий узел

    return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.value]

def postorder_reqursive(root: Node):
    """обратный обход"""
    if root:
        postorder_reqursive(root.left)
        postorder_reqursive(root.right)
        print(root.value)



def get_tree(Node):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

root = get_tree(Node)

# result = pre_order_travelsal(root)
# result_ = in_order_travelsal(root)
# _result = post_order_traversal(root)
# print(result)
# print(result_)
# print(_result)

result = postorder_reqursive(root)