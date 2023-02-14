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

S = stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
S.pop()
print("size:" ,S.size())
print("peek:",S.peek())
    