height = [2,3,4,5,18,17,6]
pre_area = 0
i,j = 0,len(height)-1
while i<=j:
    h = min(height[i],height[j])
    w = j-i
    area = h*w
    max_area = max(pre_area,area)
    pre_area = max_area
    if height[i]>height[j]:
        j-=1
    else:
        i+=1
print(pre_area)