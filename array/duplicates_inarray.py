def find_duplicates(arr):
    result = set()
    duplicates = set()
    for i in arr:
        if i in result:
            duplicates.add(i)
        else:
            result.add(i)
    return duplicates,result

array =[1,2,3,4,5,3,2,1]
duplicates,result = find_duplicates(array)
print("the duplicates values in array are : ",duplicates)
print("the values in array are : ",result)
