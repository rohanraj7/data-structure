# class solution:
#     def twosum(self,nums,target):
#         num_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement],i]
#             num_map[num] = i
            
    
# sol = solution()
# param_1 = [1,2,4,5,3,6]
# param_2 =  4
# ret = sol.twosum(param_1,param_2)  
# print(ret)
  
class solution:
    def twosum(self,nums,target):
        num_map ={}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement],i]
            num_map[num] = i
sol = solution()
param_1 = [1,2,4,5,3,6]
param_2 = 4
ret = sol.twosum(param_1,param_2)
print(ret)            

   
 