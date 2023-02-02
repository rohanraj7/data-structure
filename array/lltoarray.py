class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
def arraytoll(head):
    arr = []
    current = head
    while current is not None:
        arr.append(current.data)        
        current = current.ref
    return arr
def print_ll(arr):
    print(*arr)
 
linked_list = Node(1)
linked_list.ref = Node(10)
linked_list.ref.ref = Node(20)
linked_list.ref.ref.ref = Node(30)
linked_list.ref.ref.ref.ref = Node(40)
linked_list.ref.ref.ref.ref.ref = Node(50)
arr = arraytoll(linked_list)
print_ll(arr)




         