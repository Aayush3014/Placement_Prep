# 692. Top K Frequent Words

import collections
words = ["i","love","leetcode","i","love","coding"]
k = 3
lst = []
hashmap = collections.Counter(words)
sorted_hashmap = sorted(hashmap.items(),key= lambda x : x[1],reverse = True)
converted_hashmap = dict(sorted_hashmap)

for key,value in converted_hashmap.items():
	lst.append(key)
	k-=1
	if k==0:
		break
		


print(lst)