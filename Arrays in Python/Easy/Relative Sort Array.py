arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

# Output: [2,2,2,1,4,3,3,9,6,7,19]
lst = []
for i in arr2:
    count = arr1.count(i)
    for j in arr1:
        if j == i:
            lst.append(i)
            # arr1.remove(i)
            if arr1.count(i) == lst.count(i):
                arr1.remove(ai)
                break
        
for k in arr1:
    if k not in lst:
        lst.append(k)
        arr1.remove(k)
        # else:
        #     pass
print(lst)
print(arr1)