from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            taken = 0
            dp[i] = float("-inf")

            for count in range(1, 4):
                if i + count > n:
                    break

                taken += stoneValue[i + count - 1]
                dp[i] = max(dp[i], taken - dp[i + count])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"