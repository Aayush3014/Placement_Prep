matrix = [[1,2,3],[4,5,6],[7,8,9]]
# [[1,4,7],[2,5,8],[3,6,9]]
m = len(matrix)
n = len(matrix[0])

ans = [[0]*m for i in range(n)]

for i in range(m):
    for j in range(n):
        ans[j][i] = matrix[i][j]

print(ans)