nums = [1,2,2,5,3,5]
a = []
for i in nums:
    if i not in a:
        a.append(i)
length = len(a)
if length>2:
    print(a[2])
else:
    print(max(a))
print(a)