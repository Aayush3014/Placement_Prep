nums = [1,2,1,3,2,5]
xor = nums[0]
result = []
for i in nums:
	xor ^= i
	if xor == 0:
		result.append(i)
print(xor)
print(result)