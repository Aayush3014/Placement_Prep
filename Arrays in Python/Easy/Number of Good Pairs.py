nums =  [1,1,1,1]
n = len(nums)
count = 0
for i in range(n):
    for j in range(1,n):
        if nums[i] == nums[j] and i<j:
            count+=1
print(count)
