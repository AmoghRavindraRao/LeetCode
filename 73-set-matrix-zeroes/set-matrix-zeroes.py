class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = set()
        row = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if 0 in matrix[i]:
                for j in range(n):
                    if matrix[i][j] == 0:
                        col.add(j)
                    else:
                        matrix[i][j] = 0
            else: 
                row.add(i)
        for i in list(row):
            for j in list(col):
                matrix[i][j] = 0
