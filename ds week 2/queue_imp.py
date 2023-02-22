class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        self.queue.pop(0)
    def print(self):
        print(self.queue)
        
Q = Queue()        
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.dequeue()
# Q.print()
print(Q.queue)
