array = [1,2,3]
n = (len(array)*2)
result = [0] * (len(array)*2)
for i in range(len(array)*2):
    result[i] = array[i%len(array)]
print(result)