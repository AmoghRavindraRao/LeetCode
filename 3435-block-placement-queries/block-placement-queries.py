class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        max_x = max(q[1] for q in queries)

        # Fenwick tree: stores which positions currently have obstacles.
        n = max_x + 2
        bit = [0] * (n + 1)

        def add(i, delta):
            while i <= n:
                bit[i] += delta
                i += i & -i

        def prefix_sum(i):
            i = min(i, n)
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        def kth(k):
            """Return smallest index with prefix_sum(index) >= k."""
            idx = 0
            step = 1 << (n.bit_length() - 1)
            while step:
                nxt = idx + step
                if nxt <= n and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]
                step >>= 1
            return idx + 1

        # Segment tree: at obstacle x, store gap from previous obstacle to x.
        size = 1
        while size <= max_x:
            size <<= 1
        seg = [0] * (2 * size)

        def seg_update(pos, val):
            i = size + pos
            seg[i] = val
            i >>= 1
            while i:
                seg[i] = max(seg[i << 1], seg[i << 1 | 1])
                i >>= 1

        def seg_query(left, right):
            if left > right:
                return 0
            left += size
            right += size
            ans = 0
            while left <= right:
                if left & 1:
                    ans = max(ans, seg[left])
                    left += 1
                if not (right & 1):
                    ans = max(ans, seg[right])
                    right -= 1
                left >>= 1
                right >>= 1
            return ans

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                before = prefix_sum(x - 1)
                prev_obstacle = kth(before) if before else 0

                up_to_x = prefix_sum(x)
                total = prefix_sum(max_x)
                next_obstacle = kth(up_to_x + 1) if up_to_x < total else None

                seg_update(x, x - prev_obstacle)

                if next_obstacle is not None:
                    seg_update(next_obstacle, next_obstacle - x)

                add(x, 1)

            else:
                x, sz = q[1], q[2]

                count = prefix_sum(x)
                prev_obstacle = kth(count) if count else 0

                best_gap = max(
                    seg_query(1, x),   # complete gaps ending at obstacles <= x
                    x - prev_obstacle  # tail gap from last obstacle to x
                )

                ans.append(best_gap >= sz)

        return ans