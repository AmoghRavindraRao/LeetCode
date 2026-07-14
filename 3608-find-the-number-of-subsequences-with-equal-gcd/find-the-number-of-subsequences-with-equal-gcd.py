class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        limit = max(nums)
        width = limit + 1

        dp = [0] * (width * width)
        dp[0] = 1

        for x in nums:
            next_gcd = [gcd(g, x) for g in range(width)]
            new_dp = dp[:]

            for g1 in range(width):
                row = g1 * width
                new_g1_row = next_gcd[g1] * width

                for g2 in range(width):
                    count = dp[row + g2]
                    if count == 0:
                        continue

                    # Add x to seq1.
                    index = new_g1_row + g2
                    new_dp[index] = (
                        new_dp[index] + count
                    ) % MOD

                    # Add x to seq2.
                    index = row + next_gcd[g2]
                    new_dp[index] = (
                        new_dp[index] + count
                    ) % MOD

            dp = new_dp

        answer = 0
        for g in range(1, width):
            answer = (answer + dp[g * width + g]) % MOD

        return answer