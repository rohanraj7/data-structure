n = int(input("Enter how many numbers to add"))
n1,n2 = 0,1
if n < 0:
    print("please enter the positive numbers")
if n == 0:
    print("Error")  
if n == 1:
    print("The Fibonacci series values are upto :",n)    
    print(n1)
i = 0
while i < n:
    print(n1)
    n3 = n1 + n2
    n1 = n3
    n2 = n2
    i += 1
    
    
    