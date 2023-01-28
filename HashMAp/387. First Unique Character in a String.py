# 387. First Unique Character in a String

import collections
s = "leetcode"
hashmap = collections.Counter(s)
print(hashmap)
for key,value in hashmap.items():
	if value==1:
		ans = s.index(key)
		break
print(ans)