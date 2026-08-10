class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        squares = []
        number = 1

        while number * number <= n:
            squares.append(number * number)
            number += 1

        for stones in range(1, n + 1):
            for square in squares:
                if square > stones:
                    break

                if not dp[stones - square]:
                    dp[stones] = True
                    break

        return dp[n]