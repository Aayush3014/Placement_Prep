''' 33. Search in Rotated Sorted Array'''

''' Kunal Kushwaha Detailed Solution'''
# def search(arr,target):
#     pivot = findpivot(arr)

#     # Do simple binary search as the array is not rotated.
#     if pivot==-1:    
#         return binary_search(arr, target, beg= 0, end = len(arr)-1)
    
#     # If pivot is found then we have two ascending arrays
#     if arr[pivot] == target:
#         return pivot
#     if target > arr[0]:
#         return binary_search(arr,target,0,pivot-1)
#     else:
#         return binary_search(arr,target,pivot+1,len(arr)-1)
    
# def findpivot(arr):
#     start, end = 0, len(arr)-1
    
#     while start<=end:
#         mid = (start)+(end-start)//2

#     #Now 4 cases as we discussed.
#     # CASE 1
#         if mid < end and arr[mid]>arr[mid+1]:   # first condition is used to check when the mid is last 
#             return mid                          # then if it goes index out of bounds it should not execute
#     # CASE 2    
#         if mid > start and arr[mid]<arr[mid-1]:  # reason is same as above just mid should not go less than 
#             return mid-1                         # start element
        
#     # CASE 3 
#         if arr[start]>arr[mid]:
#             end = mid-1
#         else:
#             start = mid+1
#     return -1
# def binary_search(arr,n,beg,end):

#     while beg<=end:
#         mid = (beg)+(end-beg)//2
#         if arr[mid]==n:
#             return mid
#         elif arr[mid]<n:
#             beg = mid+1
#         elif arr[mid]>n:
#             end = mid-1
#     return -1
# # Now Binary Search 
# arr = [3,5,1]
# # print(findpivot(arr))
# print(search(arr,3))


''' LeetCode Submitting Solution'''

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start, end = 0, len(nums) - 1
    
#         while start <= end:
#             mid = start + (end-start) // 2
            
#             if nums[mid] == target:
#                 return mid
            
#             elif nums[mid] >= nums[start]:
#                 if target <= nums[mid] and target >=nums[start]:
#                     end = mid - 1
#                 else:
#                     start = mid + 1
#             else:
#                 if target >= nums[mid] and target <= nums[end]:
#                     start = mid + 1
#                 else:
#                     end = mid - 1
#         return -1