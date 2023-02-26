# 852. Peak Index in a Mountain Array

def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start,end = 0,len(arr)-1
        while start < end:
            mid = start + (end-start)//2
            if arr[mid]>arr[mid+1]:
                end = mid
            else:
                start = mid+1

        return start
# Peak index Concept
# arr = [1, 2, 3, 5, 6, 4, 3, 2]

# 1) calculate the mid 
# 2) if arr[mid]>arr[mid+1]:
#         end = mid
# then you are in the decreasing array and then our mid becomes end
# 3) if arr[mid]<arr[mid+1]:
# start = mid + 1
# 
# then we will break the loop in the end both start and end and return either start or end as both are equal
