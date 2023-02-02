# my_list = [1,2,3,4,5]
# my_list.reverse()
# for element in my_list:
#     print(element)

# from collections import deque
# arr = [1,2,3,4,5]
# linked_list = deque(arr)

# linked_list.extend([9,7,5])
# print(list(linked_list))



def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))
