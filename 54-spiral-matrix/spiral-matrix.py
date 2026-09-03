class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])
        arr = []

        i, j = m - 1, n - 1  # bottom row, right column
        r, c = 0, 0          # top row, left column

        while r <= i and c <= j:
            # Top row
            for k in range(c, j + 1):
                arr.append(matrix[r][k])

            # Right column
            for k in range(r + 1, i + 1):
                arr.append(matrix[k][j])

            # Bottom row
            if r < i:
                for k in range(j - 1, c - 1, -1):
                    arr.append(matrix[i][k])

            # Left column
            if c < j:
                for k in range(i - 1, r, -1):
                    arr.append(matrix[k][c])

            r += 1
            c += 1
            i -= 1
            j -= 1

        return arr