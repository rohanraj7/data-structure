def first_non_repeating_char(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char in s:
        if counts[char] == 1:
            return char
    return None

s = 'e,r,t,y,e,r,t'
print(first_non_repeating_char(s))