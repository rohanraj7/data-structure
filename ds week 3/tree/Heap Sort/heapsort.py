def heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)
    
def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
        
def find_second_largest_even_numbers(arr):
    evens = [num for num in arr if num%2 == 0]
    
    if len(evens) < 2:
        return
    
    heapsort(evens)
    
    return evens[-2]
        
arr = [22,5,77,44,3,11,77,55,99,2,1]
heapsort(arr)
print(arr)
print(find_second_largest_even_numbers(arr))
        