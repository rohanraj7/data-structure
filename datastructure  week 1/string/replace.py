# def replace_alphabets(s, n):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     result = ""
#     for char in s:
#         if char.lower() in alphabet:
#             index = alphabet.index(char.lower())
#             new_index = (index + n) % 26
#             result += alphabet[new_index].upper() if char.isupper() else alphabet[new_index]
#         else:
#             result += char
#     return result

# s = "Hello World"
# n = 5

# print(replace_alphabets(s, n))



def replace_alphabets(s,n):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in s:
        if char.lower() in alphabets:
            index = alphabets.index(char.lower())
            new_index = (index + n) % 26
            result += alphabets[new_index].upper() if char.isupper() else alphabets[new_index]
        else:
            result += char
    return result        
s = "Man"
n = 2
print(replace_alphabets(s,n))     


       