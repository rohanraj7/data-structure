def bublesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1],arr[j]
    return arr

arr = [11,55,33,88,22,44] 
print("The sorted list of array of bubble is :" ,bublesort(arr))    

                