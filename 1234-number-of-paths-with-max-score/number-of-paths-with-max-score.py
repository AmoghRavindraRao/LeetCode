class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        count[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    continue

                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni >= n or nj >= n:
                        continue
                    if score[ni][nj] == -1:
                        continue

                    val = 0 if board[i][j] in 'ES' else int(board[i][j])
                    new_score = score[ni][nj] + val

                    if new_score > score[i][j]:
                        score[i][j] = new_score
                        count[i][j] = count[ni][nj]
                    elif new_score == score[i][j]:
                        count[i][j] = (count[i][j] + count[ni][nj]) % MOD

        if count[0][0] == 0:
            return [0, 0]

        return [score[0][0], count[0][0] % MOD]