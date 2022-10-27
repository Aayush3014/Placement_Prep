# #

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         lst = [1]*len(nums)
#         pre = 1
#         for i in range(len(nums)):
#             lst[i] = pre
#             pre*=nums[i]
            
#         post = 1
#         for i in range(len(nums)-1, -1, -1):
#             lst[i]*=post
#             post *= nums[i]
#         return lst