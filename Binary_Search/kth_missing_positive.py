arr = [1,2,3]
k = 5
count = 0
n = len(arr)
i,j = 0,1
while i<n:
    if arr[i]!=j:
        count += 1
        if count == k:
            print(j)
        j+=1
    else:
        i+=1
        j+=1
print(arr[-1]+k-count)