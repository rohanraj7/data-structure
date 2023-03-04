class MaxHeap:
    def __init__(self,items):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.floatup(len(self.heap)-1)
    def push(self,data):
        self.heap.append(data)
        self.floatup(len(self.heap)-1)
    def peek(self):
        if self.heap[1]:
            return True
        else:
            return False
    def pop(self):
        if len(self.heap) > 2:
            self.swap(1,len(self.heap)-1)
            maxi = self.heap.pop()
            self.doubledown(1)
        elif len(self.heap) == 2:
            maxi = self.heap.pop()
        else:
            maxi = False
        return maxi
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    def floatup(self,index):
        parent = index//2
        if index <= 1:
            return 
        elif self.heap[index] > self.heap[parent]:
            self.swap(index,parent)
            self.floatup(parent)
    def doubledown(self, index):
        left = index*2
        right = index*2+1
        largest = index
        if len(self.heap)>left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap)>right and self.heap[largest] < self.heap[right]:
            largest = right 
        if largest!=index:
            self.swap(index,largest)
            self.doubledown(largest)

MAX = MaxHeap([54,2,56,6,8])
MAX.push(10)
print(MAX.heap[1:len(MAX.heap)])
print(MAX.pop())