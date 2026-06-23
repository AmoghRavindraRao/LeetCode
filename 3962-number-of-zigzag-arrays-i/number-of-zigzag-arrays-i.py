class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1

        up = [1] * m
        down = [1] * m

        for _ in range(1, n):
            new_up = [0] * m
            new_down = [0] * m

            # If next must go up, y can follow any smaller x.
            prefix = 0
            for y in range(m):
                new_down[y] = prefix
                prefix = (prefix + up[y]) % MOD

            # If next must go down, y can follow any larger x.
            suffix = 0
            for y in range(m - 1, -1, -1):
                new_up[y] = suffix
                suffix = (suffix + down[y]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD