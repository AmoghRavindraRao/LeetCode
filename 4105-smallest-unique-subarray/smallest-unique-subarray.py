class Solution:
    def smallestUniqueSubarray(self, A: List[int]) -> int:
        res = n = len(A)
        b = 215215
        mod = (1 << 31) - 1
        l, r = 1, n
        while l < r:
            k = (l + r) // 2
            h, p = 0, 1
            for i in range(k):
                h = (h * b + A[i]) % mod
                p = (p * b) % mod
            c = Counter([h])
            for i in range(k, n):
                h = (h * b + A[i] - A[i - k] * p) % mod
                c[h] += 1
            if 1 in c.values():
                r = k
            else:
                l = k + 1
        return l        