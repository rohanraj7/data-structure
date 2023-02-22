class stack:
    def __init__(self):
        self.item = []
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def peek(self):
        return self.item[-1]
    def size(self):
        return len(self.item)
    def stackmid(self):
        n = len(self.item)//2
        self.item.pop(n)
S = stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
# S.pop()
# S.stackmid()
# print(S.peek)
print(S.item)

    