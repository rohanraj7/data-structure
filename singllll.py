class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class sLinkedlist:
    def __init__(self):
        self.head = None
    def printll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data,"-->",end=" ")            
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
    
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")    
            return
        else:
            self.head = self.head.ref
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")    
            return
        if self.head.ref is None:
            self.head.ref = None
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = None    
    def delete_byvalue(self,data):
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

sol = sLinkedlist()
sol.add_begin(10)
sol.add_begin(20)
sol.add_begin(30)
sol.add_begin(40)
sol.add_begin(50)
sol.add_end(60)
sol.add_end(70)
sol.delete_byvalue(60)
sol.printll()                
                        
                            
                
            
        