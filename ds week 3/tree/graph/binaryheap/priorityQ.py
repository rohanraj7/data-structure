class BinaryHeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        self.heap.append((value, priority))
        self._bubble_up(len(self.heap) - 1)

    def pop_min(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_value

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][1] < self.heap[parent_index][1]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while 2 * index + 1 < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2 if 2 * index + 2 < len(self.heap) else None
            min_child_index = left_child_index
            if right_child_index and self.heap[right_child_index][1] < self.heap[left_child_index][1]:
                min_child_index = right_child_index
            if self.heap[min_child_index][1] < self.heap[index][1]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

q = BinaryHeapPriorityQueue()
q.insert("task1", 3)
q.insert("task2", 2)
q.insert("task3", 1)
q.insert("task4",4)
print(q.heap)
print(q.pop_min()) # ("task3", 1)
print(q.heap)
 
print(q.pop_min()) # ("task2", 2)
print(q.pop_min()) # ("task1", 3)
