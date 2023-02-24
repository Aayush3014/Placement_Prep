def Floor_of_number(arr,n):     # Floor is greatest number <= target 
    
    # If the target number is smaller than the smallest element in the array
    # then we use 
    if n<arr[0]:
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
    return end

a = [2,6,9,58,96]
n = -5
print(Floor_of_number(a,n))
