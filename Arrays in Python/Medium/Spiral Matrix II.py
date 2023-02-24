n = 3

# creating empty square matrix
# i is for rows 
# j is for columns
ans = [[0 for i in range(n)] for j in range(n)]


left = 0
right = n-1
top = 0
down = n-1
val = 1     

# while condition is for looping through the loop till left and top does not overlap with right 
# and down.

while top<=down and left<=right :

    # for iterating over first row and inserting value of val 
    for i in range(left,right + 1):
        ans[top][i] = val
        val += 1    # incrementing value of val 
            

    # for iterating over last column and inserting value of val        
    for i in range(top + 1, down + 1): # here top + 1 is used bcz we want to ignore the element 
                                       # which is already inserted.
        ans[i][right] = val
        val+=1
            
            
            
    for i in reversed(range(left,right)):
        if top == down:
            break
        ans[down][i] = val
        val += 1
            
            
    for i in reversed(range(top+1,down)):
        if left == right:
            break
        ans[i][left] = val
        val+=1
                
    top+=1
    right -= 1
    down -= 1
    left +=1

print(ans)