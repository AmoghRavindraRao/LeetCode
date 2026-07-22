class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count("1")

        start, end, char, run_id = [], [], [], [0] * n
        i = 0

        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1

            idx = len(char)
            start.append(i)
            end.append(j)
            char.append(s[i])

            for k in range(i, j + 1):
                run_id[k] = idx

            i = j + 1

        m = len(char)

        gain = [0] * m
        for j in range(1, m - 1):
            if char[j] == "1":
                gain[j] = (
                    end[j - 1] - start[j - 1] + 1 +
                    end[j + 1] - start[j + 1] + 1
                )

        size = 1
        while size < m:
            size *= 2

        tree = [0] * (2 * size)
        tree[size:size + m] = gain

        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def range_max(left, right):
            if left > right:
                return 0

            left += size
            right += size
            result = 0

            while left <= right:
                if left % 2:
                    result = max(result, tree[left])
                    left += 1
                if right % 2 == 0:
                    result = max(result, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return result

        def boundary_gain(j, left, right):
            if j <= 0 or j >= m - 1 or char[j] != "1":
                return 0

            left_zeros = end[j - 1] - max(left, start[j - 1]) + 1
            right_zeros = min(right, end[j + 1]) - start[j + 1] + 1

            return max(0, left_zeros) + max(0, right_zeros)

        answer = []

        for left, right in queries:
            first = run_id[left]
            last = run_id[right]
            best = 0

            if last - first >= 2:
                best = max(
                    best,
                    boundary_gain(first + 1, left, right),
                    boundary_gain(last - 1, left, right)
                )
                best = max(best, range_max(first + 2, last - 2))

            answer.append(total_ones + best)

        return answer