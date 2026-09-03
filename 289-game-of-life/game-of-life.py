class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        temp = [row[:] for row in board]  

        def ones(r, c):
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and abs(temp[nr][nc]) == 1:
                        count += 1
            return count         
        for i in range(m):
            for j in range(n):
                count = ones(i, j)

                if temp[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                elif count == 3:
                    board[i][j] = 1
                        

                