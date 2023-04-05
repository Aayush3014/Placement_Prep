# Two binary searches will be used.

nums = [1,1,1,1,1,0,0,0]
target = 1
def binarysearchLeft(arr,n):
    start,end = 0,len(arr)-1
    while start<=end:
        mid = start + (end-start)//2

        if n > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return start

def binarysearchRight(arr,n):
    start,end = 0,len(arr)-1
    while start<=end:
        mid = start + (end-start)//2

        if n >= arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return end

left, right = binarysearchLeft(nums, target), binarysearchRight(nums, target)
# return (left, right) if left <= right else [-1, -1]
print(right-left+1)