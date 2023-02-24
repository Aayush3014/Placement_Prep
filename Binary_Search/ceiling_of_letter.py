letter = [3,6,10]
target = 1
beg = 0
end = len(letter)-1
ans = 0

while beg<=end:
    mid = (beg+end)//2
    if mid == target:
        ans =  beg+1
    elif mid > target:
        beg = mid + 1
    elif mid<target:
        end = mid-1
print(ans)