def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key  
    return arr


arr = [22,11,23,88,55,38]
print("The value is sorted in correct : ",insertionsort(arr))