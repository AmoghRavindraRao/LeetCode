class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp = [row[:] for row in matrix]
        for i in range(n):
            for j in range(n):
                matrix[j][n - i - 1] = temp[i][j]
        

        