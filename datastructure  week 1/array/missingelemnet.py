a = [1,2,3,4,5,6,7,9,10]
missing = []

for i in range(len(a)-1):
    if a[i+1] - a[i] != 1:
        missing.append(a[i]+1)
print("Missing Element is ", missing)
