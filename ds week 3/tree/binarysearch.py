class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left_child:
                self._insert(node.left_child, value)
            else:
                node.left_child = Node(value)
        else:
            if node.right_child:
                self._insert(node.right_child, value)
            else:
                node.right_child = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node:
            if node.value == value:
                return True
            elif value < node.value:
                return self._search(node.left_child, value)
            else:
                return self._search(node.right_child, value)
        return False

tree = BinarySearchTree(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(7)
print(tree.search(5)) # True
print(tree.search(8)) # False
