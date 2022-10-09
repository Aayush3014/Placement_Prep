class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums2 = []
        for i in range(len(nums)):
            a = nums[nums[i]]
            if a not in nums2:
                nums2.append(a)
        return nums2