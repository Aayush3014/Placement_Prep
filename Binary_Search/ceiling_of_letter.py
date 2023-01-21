letter = ["c","f","j"]
target = "a"
beg = 0
end = len(letter)-1

if target<letter[0] or target>letter[-1]:
    # lst.append(letter[0])
    return letter[0]
while beg<=end:
    mid = (beg+end)//2
    # if letter[mid]==target:
    #     print(letter[mid])
    # else:
    if target>=letter[mid]:
        beg = mid + 1
    if target<letter[mid]:
        end = mid-1
        
#     print(letter[end])
# else:
#     print(letter[0])
return letter[beg]

"""
# if the number is out of bound
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = (high+low)//2
            
            if  target >= letters[mid]: # in binary search this would be only greater than
                low = mid+1
            
            if target < letters[mid]:
                high = mid-1
                
        return letters[low]"""