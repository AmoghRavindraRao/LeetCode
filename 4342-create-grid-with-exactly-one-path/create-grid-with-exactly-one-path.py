class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        grid.append('.'*n)
        for i in range(1,m):
            temp = '#'*(n - 1)
            grid.append(temp + '.')
        return grid