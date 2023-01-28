def reversestring(str):
    n = len(str)
    i = n-1
    str1 = ''
    while i > 0:
        str1 += str[i]
        i -= 1
    print(str1)    

str = 'codecheater55'    
reversestring(str)