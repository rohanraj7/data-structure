class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)    
        else:
            if self.right:
                self.right.insert(data)        
            else:
                self.right = Node(data)    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")    
        if self.right:
            self.right.inorder()
    def preOrder(self):
        print(self.key,end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()            
        print(self.key, end=" ")
    def searchkey(self,data):
        if self.key == data:
            print("Node is present")        
            return
        if self.key < data:
            if self.right:
                self.right.searchkey(data)
            else:
                print("Node is not present")
        else:
            if self.left:
                self.left.searchkey(data)            
            else:
                print("Node is not present")    
    def level_order(self):
        if self is None:
            return
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.key, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)            
    
    def deleteNode(self,data):
        if self.key is None:
            print("Node is not present")
            return
        if data < self.key:
            if self.left:
                self.left = self.left.deleteNode(data)
            else:
                print("Node is not present")
        elif data > self.key:
            if self.right:
                self.right = self.right.deleteNode(data)
            else:
                print("Node is not present")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.deleteNode(node.key)    
        return self
    def find_close_value(self,target):
        if self.key is None:
            return None
        if self.key == target:
            return self.key
        if target < self.key:
            if self.left:
                closest = self.left.find_close_value(target)
            else:
                closest = self.key    
        else:
            if self.right:
                closest = self.right.find_close_value(target)    
            else:
                closest = self.key    
        if abs(self.key - target) < abs(closest - target):
            return self.key
        return closest
                                
    def is_bst(self):
        if self is None:
            return True
        if self.left is not None and self.left.key > self.key:
            return False
        if self.right is not None and self.right.key < self.key:
            return False
        if (self.left and not self.left.is_bst()) or (self.right and not self.right.is_bst()):
            return False
        return True
        
            
                          
root = Node(8)
q = [100,30,25,10,12,5,3,7]
for i in q:
    root.insert(i)
root.inorder()   
print()
root.preOrder() 
print()
root.postorder()
print()
root.searchkey(11)
root.inorder()
print()
root.deleteNode(333)
root.inorder()
print()
root.searchkey(1000)
print(root.find_close_value(10))

if root.is_bst():
    print("the tree is binary search tree") 
else:
    print("the tree is Not")    
print()
root.level_order()

                