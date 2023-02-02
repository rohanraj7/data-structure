
def removeduplicates(array):
    duplicates = set()
    for i in range(len(array)):
        if array[i] in duplicates:
            array[i] = -1
        else:
            duplicates.add(array[i])
                
    i = 0
    while i < len(array):
        if array[i] == -1:
            del array[i]
        else:
            i += 1
    return array
array = [1,2,3,4,5,6,7,2,4,6]
result = removeduplicates(array)
print(result)        
                
                
class Node:
    def __init__(self,data,ref=None):
        self.data = data 
        self.ref = ref
class Array_toLl:
    def arraytoll(self,array):
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
sol = Array_toLl()
rr = sol.arraytoll(result)
sol.print_ll(rr)