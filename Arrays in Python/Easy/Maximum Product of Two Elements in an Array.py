nums = [1,5,4,5]
lst = []
sum = 0
for i in range(0,len(nums),1):
    for j in range(1,len(nums),1):
        if i == j:
            pass
        else:
            sum = (nums[i]-1)*(nums[j]-1)
            lst.append(sum)
print(max(lst))


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return (nums[-1]-1)*(nums[-2]-1)