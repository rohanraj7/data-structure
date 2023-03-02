class MinHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
        
    def heapify_up(self, idx):
        parent_idx = (idx-1)//2
        if parent_idx >= 0 and self.heap[parent_idx] > self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self.heapify_up(parent_idx)
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val
    
    def heapify_down(self, idx):
        left_child_idx = 2*idx + 1
        right_child_idx = 2*idx + 2
        smallest_child_idx = idx
        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[smallest_child_idx]:
            smallest_child_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest_child_idx]:
            smallest_child_idx = right_child_idx
        if smallest_child_idx != idx:
            self.heap[idx], self.heap[smallest_child_idx] = self.heap[smallest_child_idx], self.heap[idx]
            self.heapify_down(smallest_child_idx)
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(7)
min_heap.insert(1)
min_heap.insert(9)
min_heap.insert(2)

print(min_heap.heap) # Output: [1, 3, 2, 5, 9, 7]
