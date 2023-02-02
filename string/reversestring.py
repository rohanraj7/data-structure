# def reversestring(str):
#     n = len(str)
#     i = n-1
#     str1 = ''
#     while i > 0:
#         str1 += str[i]
#         i -= 1
#     print(str1)    

# str = 'codecheater55'  
# print(str)  
# reversestring(str)

arr = 'HELLO'
print(arr)
arr = list(arr)
temp = arr[0]
arr[0] = arr[1]
arr[1] = temp
print("".join(arr))
