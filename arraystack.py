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
