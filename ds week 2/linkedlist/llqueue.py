class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.rear = None
    def is_empty(self):
        return self.front == None
    
    def enqueue(self,item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
    def dequeue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
        if (self.front == None):
            self.rear = None
    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data,"-->",end=" ")
            temp = temp.next
        print()        
            
q = Queue()            
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.enqueue(100)
q.display()




            