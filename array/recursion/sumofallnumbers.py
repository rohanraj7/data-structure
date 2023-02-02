def sum_of_numbers(numbers,index=0):
    if index == len(numbers):
        return 0
    else:
        return numbers[index] + sum_of_numbers(numbers, index+1)
array =[1,2,3,4,5]
print(sum_of_numbers(array))    