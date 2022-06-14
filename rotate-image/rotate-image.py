class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Variable declaration here
        # Get the number of columns 
        n = len(matrix[0])
        
        for i in range(n // 2 + n % 2):
            for j in range(n//2):
                temp = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i -1]
                matrix[j][n - i -1] = matrix[i][j]
                matrix[i][j] = temp 
                