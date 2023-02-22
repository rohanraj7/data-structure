class ArrayStack:
    def __init__(self):
        self.array = []   # Initialize the array to an empty list
        self.top = -1     # Initialize the top index to -1 to indicate an empty stack

    def push(self, element):
        self.top += 1             # Increment the top index
        self.array.append(element)  # Add the element to the end of the array

    def pop(self):
        if self.top == -1:        # If the stack is empty, return None
            return None
        element = self.array.pop()   # Remove the last element from the array
        self.top -= 1             # Decrement the top index
        return element

    def peek(self):
        if self.top == -1:        # If the stack is empty, return None
            return None
        return self.array[self.top]  # Return the last element in the array

    def is_empty(self):
        return self.top == -1     # Return True if the stack is empty, False otherwise
stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())    
print(stack.pop())     
print(stack.pop())     
print(stack.is_empty())
print(stack.pop())     
print(stack.is_empty())
print(stack.pop())     
print(stack.array)

# Output: 3
# Output: 3
# Output: 2
   # Output: False
# Output: 1
   # Output: True
# Output: None




            