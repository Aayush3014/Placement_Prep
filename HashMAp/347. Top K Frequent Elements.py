import collections
nums = [1,1,1,2,2,3]
k = 2
lst = []
hashmap = collections.Counter(nums)
sorted_hashmap = sorted(hashmap.items(),key= lambda x : x[1],reverse = True)
converted_hashmap = dict(sorted_hashmap)
# print(converted_hashmap)
# for i in range(k):
# 	lst.append(converted_hashmap[i])
# while k>0:
# 	lst.append(converted_hashmap[])

for key,value in converted_hashmap.items():
	lst.append(key)
	k-=1
	if k==0:
		break
		


print(lst)