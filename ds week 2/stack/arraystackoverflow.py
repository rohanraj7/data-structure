class ArrayStack:
    def __init__(self, capacity):
        self.array = [None] * capacity  # Initialize the array to the specified capacity
        self.top = -1                  # Initialize the top index to -1 to indicate an empty stack
        self.capacity = capacity       # Store the maximum capacity of the stack

    def push(self, element):
        if self.top == self.capacity - 1:  # If the stack is full, print an error message and exit the program
            print("Stack overflow")
            exit(1)
        self.top += 1                # Increment the top index
        self.array[self.top] = element   # Add the element to the array at the current top index

    def pop(self):
        if self.top == -1:           # If the stack is empty, return None
            return None
        element = self.array[self.top]   # Remove the last element from the array
        self.array[self.top] = None  # Set the array element to None to free the memory
        self.top -= 1                # Decrement the top index
        return element

    def peek(self):
        if self.top == -1:           # If the stack is empty, return None
            return None
        return self.array[self.top]  # Return the last element in the array

    def is_empty(self):
        return self.top == -1        # Return True if the stack is empty, False otherwise


connect = ArrayStack(3)
connect.push(1)
connect.push(2)
connect.push(3)
print(connect.pop())
print(connect.peek())
# print(connect.is_empty())