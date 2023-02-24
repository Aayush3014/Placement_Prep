nums = [2,5,1,3,4,7]
n = len(nums)//2

new_list = []
for i in range(n):
    new_list.append(nums[i])
    new_list.append(nums[i+n])
print(new_list)