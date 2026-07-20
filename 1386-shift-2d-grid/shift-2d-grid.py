class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        totalElements = rows * cols

        k = k % totalElements

        if k == 0:
            return grid
        
        flatList = [val for row in grid for val in row]

        shiftedList = flatList[-k:] + flatList[:-k]

        res = []

        for i in range(0, totalElements, cols):
            rowChunk = shiftedList[i: i + cols]
            res.append(rowChunk)
        return res