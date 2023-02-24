# Output: "a"

# arr = ["d","b","c","b","c","a"]
# k = 2
# arr = ["aaa","aa","a"]
# k = 1
from collections import Counter

arr = ["a","b","a"]
k = 3
result = [] 
if k>len(arr):
	print("54")
else:
	hashmap = Counter(arr)
# print(hashmap)
	for key,value in hashmap.items():
		if value==1:
			result.append(key)

	# print(result[k-1])