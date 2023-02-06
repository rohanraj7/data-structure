# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None
# def arraytolinked_list(array):
#     head = Node(array[0])
#     current = head
#     for i in range(1, len(array)):
#         current.ref = Node(array[i])
#         current = current.ref
#     return head
# def print_ll(head):
#     m = head
#     while m is not None:
#         print(m.data,"-->",end=" ")
#         m = m.ref
#     print("None")    
# array =[1,2,3,4,5]
# sol = arraytolinked_list(array)        
# print_ll(sol)

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class arraytoll:
    def array_to_ll(self,array):
        head = Node(array[0])
        current = head
        for i in range(1 , len(array)):
            current.ref = Node(array[i])
            current = current.ref
        return head
    def print_ll(self,head):
        m = head
        while m is not None:
            print(m.data,"-->",end=" ")
            m = m.ref
        print("None")    
array = [1,3,2,4,5]
sol = arraytoll()
head = sol.array_to_ll(array)        
sol.print_ll(head)
            
        