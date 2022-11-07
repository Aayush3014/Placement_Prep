# Brute force approach

nums = [9,12,5,10,14,3,10]
pivot = 10
# small = []
# large = []
# count = 0
# for i in nums:
#     if i==pivot:
#         count+=1
#     elif i<pivot:
#         small.append(i)
#     elif i>pivot:
#         large.append(i)
# for i in range(count):
#     small.append(pivot)
# print(small+large)

# optimized solution

arr = []
# large = []
count = 0
for i in nums:
    if i==pivot:
        count+=1
    elif i<pivot:
        arr.append(i)
for i in range(count):
    arr.append(pivot)
for i in nums:
    if i>pivot:
        arr.append(i)
# for i in range(count):
    # small.append(pivot)
print(arr)