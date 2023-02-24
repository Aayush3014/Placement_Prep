arr = [2,3,4,7,11]
k = 5
sum = 0
for i in range(1,len(arr)+1):
    if (i+k-1) not in arr:
        sum = i+k-1
print(sum)