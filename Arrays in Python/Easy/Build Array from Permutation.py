# In this nested elements is applied


nums = [0,2,1,5,3,4]
nums2 = []
for i in range(len(nums)):
    a = nums[nums[i]]
    if a not in nums2:
        nums2.append(a)
print(nums2)
