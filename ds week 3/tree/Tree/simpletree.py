class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    

tree = Node(2)
tree.left = Node(3)        
tree.right = Node(6)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(7)
tree.right.right = Node(8)

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level=level+1)
        print("    "*level + str(node.value))
        print_tree(node.left, level=level+1)

print_tree(tree)

