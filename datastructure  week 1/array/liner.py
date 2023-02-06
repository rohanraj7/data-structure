def linear_search(arr,x):
    for i in arr:
        if i == x:
            return i
    return -1

arr = [1,2,3,4,5,6]
x = 5
result = linear_search(arr,x)    
if result != -1:
    print("element found at index",str(result))
else:    
    print("element Not present in array")
    