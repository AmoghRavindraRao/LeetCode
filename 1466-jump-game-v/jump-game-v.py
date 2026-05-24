class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            best = 1

            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + dfs(j))

            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + dfs(j))

            memo[i] = best
            return best

        ans = 0

        for i in range(n):
            ans = max(ans, dfs(i))

        return ans