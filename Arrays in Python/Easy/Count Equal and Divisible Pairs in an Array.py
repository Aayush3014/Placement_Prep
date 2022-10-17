class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            
            for j in range(1,len(nums)):
                if i<j and nums[i]==nums[j] and ((i*j)%k) == 0:
                    count+=1
                else:
                    pass
        return count