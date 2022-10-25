matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = []
left, right = 0, len(matrix[0])
top, bottom = 0, len(matrix)
        
while left < right and top<bottom:
    # getting every element in top row going left to right
    for i in range(left, right):
        result.append(matrix[top][i])
    top+=1
    
    # getting every element in right col going top to bottom
    for i in range(top, bottom):
        result.append(matrix[i][right-1])
    right -= 1
    
    if not (left < right and top<bottom):
        break
    
    # getting every element in bottom row going right to left
    for i in range(right-1, left-1, -1):
        result.append(matrix[bottom-1][i])
    bottom-=1

    for i in range(bottom-1,top-1,-1):
        result.append(matrix[i][left])
    left+=1
            
print(result)
            
                