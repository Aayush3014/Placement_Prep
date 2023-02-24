class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid = n//2
        sum = 0
        for i in range(len(mat)):
            sum +=(mat[i][i]+mat[i][n-i-1])
        if n%2==0:
            return sum
        return sum-mat[mid][mid]