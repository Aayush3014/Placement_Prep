names = ["Mary","John","Emma"]
heights = [180,165,170]
hashmap = {}
for i in range(len(names)):
    if i not in hashmap:
        hashmap[names[i]] = heights[i]

c = sorted(hashmap.items(),key=lambda x:x[1],reverse = True)
a, b = zip(*c)

print(list(a))