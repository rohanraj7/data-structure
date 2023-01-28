class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print__ll(self):
        if self.head is None:
            print("LINKED LIST IS EMPTY")
        else:
            n = self.head
            while n is not None:
                print(n.data,'--->',end="")
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        print("value is added succesfully")
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node    
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node    
            
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("item is not found in the current series")
        else:
            new_node = Node(data)    
            new_node.ref = n.ref
            n.ref = new_node
                
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node 
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is Not Found")
        else:
            new_node = Node(data)    
            new_node.ref = n.ref
            n.ref = new_node
                    
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is Not empty")   
    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we cant delete node")
        else:
            self.head = self.head.ref 
    def delete_end(self):
        if self.head is None:
            print("Linked is Empty") 
        elif self.head.ref is None:
            self.head = None                                       
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None    
    def delete_by_value(self,data):
        if self.head is None:
            print("Linked list is empty")    
            return
        if self.head.data == data:
            self.head = self.head.ref
            return
        i =self.head
        while i.ref is not None:
            if i.ref.data == data:
                break
            i = i.ref
        if i.ref is None:
            print("Node you serached is Empty")    
        else:
            i.ref = i.ref.ref           
            
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_before(100,40)
LL1.delete_by_value(20)
LL1.print__ll()
                        