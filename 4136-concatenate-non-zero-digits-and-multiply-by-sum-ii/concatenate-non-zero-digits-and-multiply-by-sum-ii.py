class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(s)

        # prefix_count[i] = number of non-zero digits in s[0:i]
        prefix_count = [0] * (n + 1)

        digits = []
        for i, ch in enumerate(s):
            prefix_count[i + 1] = prefix_count[i]
            if ch != '0':
                digits.append(int(ch))
                prefix_count[i + 1] += 1

        m = len(digits)

        prefix_sum = [0] * (m + 1)

        prefix_val = [0] * (m + 1)

        pow10 = [1] * (m + 1)

        for i in range(m):
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]
            prefix_val[i + 1] = (prefix_val[i] * 10 + digits[i]) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD

        ans = []

        for l, r in queries:
            left = prefix_count[l]
            right = prefix_count[r + 1]

            if left == right:
                ans.append(0)
                continue

            length = right - left

            x = (prefix_val[right] - prefix_val[left] * pow10[length]) % MOD
            digit_sum = prefix_sum[right] - prefix_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans



