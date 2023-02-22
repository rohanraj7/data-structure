class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def push(self, x):
        self.q1.append(x)
    
    def pop(self):
        n = len(self.q1)
        for i in range(n - 1):
            self.q2.append(self.q1.pop(0))
        res = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        self.q2 = []
        return res
    
    def top(self):
        n = len(self.q1)
        for i in range(n - 1):
            self.q2.append(self.q1.pop(0))
        res = self.q1.pop(0)
        self.q2.append(res)
        self.q1, self.q2 = self.q2, self.q1
        self.q2 = []
        return res
    
    def empty(self):
        return len(self.q1) == 0
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())   
print(stack.pop())   
print(stack.top())   
print(stack.empty()) 
stack.pop()
stack.pop()
print(stack.empty()) 
