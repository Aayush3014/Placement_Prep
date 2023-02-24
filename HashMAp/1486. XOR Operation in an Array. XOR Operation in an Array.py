n = 5
start = 0
xor = 0
nums = []
for i in range(n):
	nums.append(start + 2 * i)
	xor = xor^(start + 2 * i)
print(xor)

print(nums)