class Node:
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None
def is_complete_tree(root):
    if not root:
        return True
    queue = [root]
    has_no_child = False
    while len(queue) > 0:
        node = queue.pop(0)
        
        
        if node.left is None:
            has_no_child = True
        elif has_no_child:
            return False
        else:
            queue.append(node.left)
        
        
        if node.right is None:
            has_no_child = True
        elif has_no_child:
            return False
        else:
            queue.append(node.right)
    return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(is_complete_tree(root))






        