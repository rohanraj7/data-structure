a = "STRING"
result = " "
for i in a:
    result = i + result
print(result)    


def reverse(arr):
    result = ''
    for i in arr:
        result = i + result
    return result    
arr = 'string'
print(reverse(arr))