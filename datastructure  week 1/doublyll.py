class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
        
class Doublyll:
    def __init__(self):
        self.head = None
    
    def forwardll(self):
        if self.head is None:
            print("forwardll List is  empty")
        else:       
            n = self.head
            while n is not None:
                print(n.data,"-->", end=" ")
                n = n.nref
    
    def backwardll(self):
        print()
        if self.head is None:
            print("backwardll List is empty")
        else:    
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"-->", end=" ")
                n = n.pref
                
    def insert_emptyll(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not Empty")
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.nref = new_node
        new_node.pref = n
    def add_after(self,data,x):
        if self.head is None:
            print("linked List is empty")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in Dll")
            else:
                new_node = Node(data)    
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    print("presented")
                    n.nref.pref = new_node
                n.nref = new_node
    
    def add_before(self,data,x):
        if self.head is None:
            print("Linked is Empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("given Node is Not present")    
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node    
                n.pref = new_node    
                    
         
                         
sol = Doublyll()
sol.add_begin(4)
sol.add_before(10,4)
# sol.add_after(100,1000)
sol.forwardll()
sol.backwardll()
        
                        
                                          