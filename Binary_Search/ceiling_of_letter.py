def Ceiling_of_Letter(arr,n):   # Ceiling is smallest number >= target
    beg = 0
    end = len(arr)-1
    while beg<=end:
        mid = (beg)+(end-beg)//2 
        if arr[mid]<n:
            beg = mid+1
        else:
            end = mid-1
    return arr[beg%len(arr)]

a = ['c','f','j']
n = 'j'
print(Ceiling_of_Letter(a,n))
