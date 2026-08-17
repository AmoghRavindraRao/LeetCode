from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i, value in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + value

        dp = [[0] * n for _ in range(n)]

        left_best = [[0] * n for _ in range(n)]

        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for i in range(n - 2, -1, -1):
            middle = i + 1

            for j in range(i + 1, n):
                interval_total = prefix[j + 1] - prefix[i]

                while (
                    middle <= j
                    and 2 * prefix[middle] < prefix[i] + prefix[j + 1]
                ):
                    middle += 1

                if middle == j + 1:
                    dp[i][j] = left_best[i][j - 1]

                else:
                    best = right_best[middle][j]

                    left_sum = prefix[middle] - prefix[i]
                    right_sum = prefix[j + 1] - prefix[middle]

                    if left_sum == right_sum:
                        best = max(best, left_best[i][middle - 1])

                    elif middle - 2 >= i:
                        best = max(best, left_best[i][middle - 2])

                    dp[i][j] = best

                score_if_whole_interval_is_kept = interval_total + dp[i][j]

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    score_if_whole_interval_is_kept
                )

                right_best[i][j] = max(
                    right_best[i + 1][j],
                    score_if_whole_interval_is_kept
                )

        return dp[0][n - 1]