class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        self.pref = None
        
class Douplly:
    def __init__(self):
        self.head = None
    def printforward(self):
        if self.head is None:
            print("linked list is Empty")            
        else:
            m = self.head 
            while m is not None:
                print(m.data,"-->",end=" ")
                m = m.ref
            print()
    def printbw(self):
        if self.head is None:
            print("linked list is Empty")            
        else:
            m = self.head 
            while m.ref is not None:
                m = m.ref       
            while m is not None:
                print(m.data,"<--",end=" ")
                m = m.pref
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:    
            new_node.ref = self.head
            self.head.pref = new_node
            self.head = new_node
            print("values are added")
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("Node is Added")
        else:
            m = self.head
            while m.ref is not None:
                m = m.ref
            if m.ref is None:
                new_node.ref = m.ref
                m.ref = new_node
                new_node.pref = m
    def add_after(self,data,x):
        if self.head is None:
            print("Linked list is Empty")
            return
        if self.head == x:
            new_node = Node(data)
            
        
sol = Douplly()
sol.add_begin(100)
sol.add_end(10)
sol.add_end(30)
sol.printforward() 
sol.printbw()                       
                
                    
                    
                     
                    
        