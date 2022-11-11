nums = [1,2,10,5,7]
ele = 0
lst = []
count = 0
for i in nums:
    if ele < i:
        ele = i
        # lst.append(i)
    else:
        # a = lst.pop(i)
        count+=1
if count==1:
    print(True)
else:
    print(False)