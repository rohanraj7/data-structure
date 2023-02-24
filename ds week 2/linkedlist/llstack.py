class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        popped = temp.data
        return popped
    
    def del_first(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            popped = self.head.data
            self.head = None
            return popped
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        popped = temp.next.data    
        temp.next = None
        return popped
            
            
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,"-->",end = ' ')
            temp = temp.next
        print()
        

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
# print(stack.del_first())
stack.pop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
stack.display()
# a = stack.peek()
# if a is None:
#     print("Stack is Empty")
# else:
#     print(a)    



                        