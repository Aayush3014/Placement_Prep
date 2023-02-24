# 2150. Find All Lonely Numbers in the Array

import collections
nums = [10,6,5,8]
lst = []
hashmap = collections.Counter(nums)
print(hashmap)
for key,value in hashmap.items():
	if value==1:
		if hashmap[key]-1 in nums or hashmap[key]+1 in nums:
			lst.append(key)
print(lst)