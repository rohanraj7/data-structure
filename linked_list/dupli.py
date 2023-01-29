class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        self.pref = None        
        
class doupli:
        def __init__(self):
            self.head = None
        def print_FW(self):
            if self.head is None:
                print('linkedlist is empty')
            else:
                l = self.head
                while l is not None:
                    print(l.data,"-->",end=" ")    
                    l = l.ref
        def print_bW(self):
            print()
            if self.head is None:
                print('linkedlist is empty')
            else:
                l = self.head
                while l.ref is not None:   
                    l = l.ref       
                while l is not None:
                    print(l.data,"-->",end=" ")         
                    l = l.pref
        
        def add_begin(self,data):            
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:    
                new_node.ref =self.head
                self.head.pref = new_node
                self.head = new_node    
        def add_end(self,data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:        
                l = self.head
                while l.ref is not None:
                    l = l.ref
                new_node = Node(data)    
                l.ref = new_node
                new_node.pref = l
        def add_after(self,data,x):
            if self.head is None:
                print('linkedlist is empty')
            if self.head.data == x:
                new_node = Node(data)
                new_node.ref = self.head
                self.head.pref = new_node
                self.head = new_node
                return
            l = self.head
            while l.ref is not None:
                if l.data == x:
                    break
                l = l.ref
            if l.ref is None:
                print("Invalid input")           
            else:
                new_node = Node(data)
                new_node.ref = l.ref
                l.ref = new_node
                new_node.pref = l    
        def add_before(self,data,x):
            if self.head is None:
                print('linkedlist is empty')
            if self.head.data == x:
                new_node = Node(data)
                new_node.ref = self.head
                self.head.pref = new_node
                self.head = new_node
                return
            l = self.head
            while l.ref is not None:
                if l.ref.data == x:
                    break
                l = l.ref    
            if l.ref is None:
                print("Invalid search")    
            else:
                new_node = Node(data)
                new_node.ref = l.ref
                l.ref.pref = new_node
                l.ref = new_node
                new_node.pref = l
                
                
                
dll = doupli()
dll.add_begin(10)
dll.add_begin(20)
dll.add_end(30)
dll.add_before(50,30)
dll.add_after(100,20)
dll.print_FW()               
dll.print_bW()
                        
                         
                    
                