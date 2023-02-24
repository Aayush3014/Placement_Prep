nums = [-1,0,1,2,-1,-4]
n = len(nums)
i = 0
j = 1
k = 2
lst = []
while n>0:
    if i!=j and i!=k and j!=k:
        if (nums[i] + nums[j] + nums[k]) == 0:
            lst.append([nums[i],nums[j],nums[k]])
            n-=1
            i+=1
            j+=1
            k+=1
    else:
        n-=1
        i+=1
        j+=1
        k+=1
print(lst)