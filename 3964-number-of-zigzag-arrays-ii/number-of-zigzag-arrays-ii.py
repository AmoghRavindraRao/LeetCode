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

        def mat_mul(A, B):
            size = len(A)
            C = [[0] * size for _ in range(size)]

            for i in range(size):
                for k in range(size):
                    if A[i][k]:
                        a = A[i][k]
                        row_b = B[k]
                        row_c = C[i]
                        for j in range(size):
                            row_c[j] += a * row_b[j]

                for j in range(size):
                    C[i][j] %= MOD

            return C

        def mat_vec_mul(A, v):
            size = len(A)
            res = [0] * size

            for i in range(size):
                total = 0
                for j in range(size):
                    total += A[i][j] * v[j]
                res[i] = total % MOD

            return res

        def apply_power(matrix, power, vector):
            while power:
                if power & 1:
                    vector = mat_vec_mul(matrix, vector)

                power >>= 1
                if power:
                    matrix = mat_mul(matrix, matrix)

            return vector

        # down2[i][j]: ways to go from value j back to "next move down"
        # after two moves, ending at value i.
        down2 = [[min(i, j) for j in range(m)] for i in range(m)]

        # up2[i][j]: symmetric version for "next move up".
        up2 = [[m - 1 - max(i, j) for j in range(m)] for i in range(m)]

        steps = n - 1

        if steps % 2 == 0:
            power = steps // 2
            start_down = [1] * m
            start_up = [1] * m
        else:
            power = steps // 2
            start_down = [i for i in range(m)]
            start_up = [m - 1 - i for i in range(m)]

        final_down = apply_power(down2, power, start_down)
        final_up = apply_power(up2, power, start_up)

        return (sum(final_down) + sum(final_up)) % MOD