nums = [6,5,4,8]
new_lst = []
n = len(nums)
for i in range(n):
    count = 0
    for j in range(n):
        if j!=i and nums[j]<nums[i]:
            count += 1
    new_lst.append(count)
print(new_lst)
