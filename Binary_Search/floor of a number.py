def binary_search(arr,n):
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
n = 90
print(binary_search(a,n))
