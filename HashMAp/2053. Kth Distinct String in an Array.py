arr = ["d","b","c","b","c","a"]
k = 2
hashmap = {}
count = -1
# key_list = []
result_arr = [""]*k
# print(result_arr)
for char in arr:
	if char in hashmap:
		hashmap[char]+=1
	else:
		hashmap[char] = 1
# print(hashmap)
for key,value in hashmap.items():
	if value == 1:
		count +=1
		result_arr[count] = key
print(result_arr[k-1])