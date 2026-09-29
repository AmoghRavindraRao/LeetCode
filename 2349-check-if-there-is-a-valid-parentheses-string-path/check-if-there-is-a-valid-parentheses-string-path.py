class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_length = m + n - 1

        if (
            grid[0][0] == ")"
            or grid[m - 1][n - 1] == "("
            or path_length % 2 == 1
        ):
            return False

        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    balances = 1
                else:
                    balances = 0

                    if i > 0:
                        balances |= dp[j]

                    if j > 0:
                        balances |= dp[j - 1]

                if grid[i][j] == "(":
                    balances <<= 1
                else:
                    balances >>= 1

                remaining = (m - 1 - i) + (n - 1 - j)

                balances &= (1 << (remaining + 1)) - 1

                dp[j] = balances

        return bool(dp[n - 1] & 1)