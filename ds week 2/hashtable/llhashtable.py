class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f"({self.key}, {self.value})"    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
    
    def search(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return None
    
    def delete(self, key):
        if not self.head:
            return
        if self.head.key == key:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node:
            if curr_node.key == key:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next
    
    def __str__(self):
        values = []
        curr_node = self.head
        while curr_node:
            values.append(str(curr_node))
            curr_node = curr_node.next
        return " -> ".join(values)        

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]
    
    def hash(self, key):
        print("sds",hash(key) % self.size)
        return hash(key) % self.size
    
    def insert(self, key, value):
        slot = self.hash(key)
        self.table[slot].insert(key, value)
    
    def search(self, key):
        slot = self.hash(key)
        return self.table[slot].search(key)
    
    def delete(self, key):
        slot = self.hash(key)
        self.table[slot].delete(key)
    
    
ht = HashTable(10)
ht.insert(1,'apple')
print("lkj")
ht.insert(2,'banana')
print("lkj")
ht.insert(5,'orange')
ht.insert(5,'pazham')
print("lkj")
print(ht.search('apple'))  # Output: 1
ht.delete(2)

for i in range(10):
    print(f"{i}: {ht.table[i]}")

# print(ht.search('banana'))  # Output: None
