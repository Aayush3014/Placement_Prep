# My code logic 
nums = [1, 2, 3, 4]
ans = []
sum = 0
for i in nums:
    sum += i
    ans.append(sum)
print(ans)


# Optimized Logic

for i in range(1,len(nums)):
    nums[i] += nums[i-1]
print(nums)