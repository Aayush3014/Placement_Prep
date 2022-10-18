class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = 0
        left_sum = 0
        
        for i in range(len(nums)):
            total_sum+=nums[i]
            
        for j in range(len(nums)):
            
            total_sum-=nums[j]
            if total_sum==left_sum:
                return j
            left_sum+=nums[j]
                
        return -1