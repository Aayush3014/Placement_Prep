def Ceiling_of_number(arr,n):   # Ceiling is smallest number >= target
    
    # If the target number is greater than the greatest element in the array
    # then we use 
    if n>arr[-1]:
        return -1
    beg = 0
    end = len(arr)-1
    while beg<=end:
        mid = (beg)+(end-beg)//2
        if arr[mid]==n:
            return f"{arr[mid]} found at index {mid}"
        elif arr[mid]<n:
            beg = mid+1
        elif arr[mid]>n:
            end = mid-1
    return beg

a = [2,6,9,58,96]
n = 96
print(Ceiling_of_number(a,n))
