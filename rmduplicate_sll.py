

class Node:
    def __init__(self,data=0,ref = None):
        self.data = data
        self.ref = ref
class linkedlist:
    def __init__(self):
        self.head = None
        
    def remove_duplicates(self):
        m = self.head
        while m is not None and m.ref is not None:
            if m.data == m.ref.data:
                m.ref = m.ref.ref
            else:
                m = m.ref 
        return self.head

    def print(self,node):
        m = node
        while m is not None:
            print(m.data)
            m = m.ref 
            
linkedlist = linkedlist()
linkedlist.head = Node(1,Node(1,Node(2,Node(3,Node(4,Node(4))))))
linkedlist.head = linkedlist.remove_duplicates()
linkedlist.print(linkedlist.head)
        
                  