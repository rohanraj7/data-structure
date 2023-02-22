def two_sum(nums,target):
    value = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in value:
            return [value[complement],i]
        value[num] = i
    return ['Not Found']    
nums = [2,4,5,7]
print(two_sum(nums,19))