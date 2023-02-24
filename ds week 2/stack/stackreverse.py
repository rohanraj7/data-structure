def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reverse_string = ''    
    
    while len(stack) > 0:
        reverse_string += stack.pop()
    return reverse_string    

string = input("Enter the String: ")
print(reverse_string(string))

